class FalseJury:
    def __eq__(self, oth):
        return False

class TrueJury:
    def __eq__(self, oth):
        return True


a = []
s = set()
for i in range(10000):
    a.append(i) # Айди один так как ели у нас есть переменная ссылающаяся на список, то она всегда должна на него ссылаться
    # тогда индекс первого списка нельзя
    s.add(id(a))
print(s)



a = ''
s = set()
for i in range(10000):
    a += 'i'
    s.add(id(a))
print(s) # Айди не так много так как можно заранее выдлеять больше памяти, и новую строку туда же класть

s1 = 'abc'
s2 = 'abc'
print(s1 is s2)

import collections
with open('book1.txt', 'r') as f:
    #count1 = collections.Counter(f.read().split())
    count2 = collections.Counter(list(map(str.strip, f.read().split())))
# print(count1)
print(count2)

#Для 32 битной системы id хватает на 2 гб всего, поэтому больше RAM не поможет. На них не чему будет указывать
# collections.Ccoun