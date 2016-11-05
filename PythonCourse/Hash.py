# str,tuple, int

def str_hash(s): #sdbm
    hash_ = 0
    for el in s:
        hash_ = ord(el) + (hash_ << 6) + (hash_ << 16) - hash_
    return hash_

def c_mul(a, b):
    #C type multiplication
    return eval(hex((int(a) * b) & 0xFFFFFFFF)[:-1])

def str_hash_v2(s): # python 2.x
    if not s:
        return 0 # empty
    value = ord(s[0]) << 7
    for char in s:
        value = c_mul(1000003, value) ^ ord(char)
    value = value ^ len(s)
    if value == -1:
        value = -2
    return value

#string_hash(PyStringObject *a)

 	    #register Py_ssize_t len;
 	    #register unsigned char *p;
 	    #register long x;
 	    #
 	    # if (a->ob_shash != -1)    #
 	    #     return a->ob_shash;
 	    # len = Py_SIZE(a);
 	    # p = (unsigned char *) a->ob_sval;
 	    # x = *p << 7;
 	    # while (--len >= 0)
 	    #     x = (1000003*x) ^ *p++;
 	    # x ^= Py_SIZE(a);
 	    # if (x == -1)
 	    #     x = -2;
 	    # a->ob_shash = x;
 	    # return x;

def str_hash_v3(s): # python 3.x
    x = ord(s[0]) << 7
    for char in s:
        x = (1000003*x) ^ ord(char)
    x ^= len(s) # Maybe Py_SIZE is size of object in bytes
    if x == -1:
        x = -2
    return x


# tuplehash(PyTupleObject *v)
# {
#     register long x, y;
#     register Py_ssize_t len = Py_SIZE(v);
#     register PyObject **p;
#     long mult = 1000003L;
#     x = 0x345678L;
#     p = v->ob_item;
#     while (--len >= 0) {
#         y = PyObject_Hash(*p++);
#         if (y == -1)
#             return -1;
#         x = (x ^ y) * mult;
#         /* the cast might truncate len; that doesn't change hash stability */
#         mult += (long)(82520L + len + len);
#     }
#     x += 97531L;
#     if (x == -1)
#         x = -2;
#     return x;
# }

def tuple_hash(t):
    x = 0x345678
    mult = 1000003
    for el in t:
        y = my_hash(el)
        if y == -1:
            return -1
        x = (x ^ y) * mult
        mult += (82520 + 2*len(t))
    x += 97531
    if x == -1:
        x = -2
    return x

# Хэш кортежа со строкой меняется каждый раз, а с числами нет

def my_hash(obj):
    if isinstance(obj, int):
        return obj if obj != -1 else -2
    elif isinstance(obj, str):
        return str_hash_v3(obj)
    elif isinstance(obj, tuple):
        return tuple_hash(obj)

print(my_hash(125))
print(my_hash('avc'))
print(my_hash((125,'avc')))