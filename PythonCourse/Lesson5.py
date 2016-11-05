import time

import pylab

# #pylab.figure()
#
init_time = time.perf_counter()
a = []
list_measurements = []
n = 10000
m = 1000
for i in range(n):
    a.append(i)
    if i % m == 0:
        list_measurements.append(time.perf_counter() - init_time)

#pylab.plot(list_measurements)
#pylab.xlabel()
#pylab.show()
#print(list_measurements[-1])
#
#
init_time = time.perf_counter()
a = set()
set_measurements = []
n = 10000
m = 1000
for i in range(n):
    a.add(i)
    if i % m == 0:
        set_measurements.append(time.perf_counter() - init_time)




x = list(range(0, n, m))
pylab.figure()
pylab.plot(x, list_measurements, label='List')
pylab.plot(x, set_measurements, label='Set')
pylab.xlabel('Size')
pylab.ylabel('Time')
pylab.legend(loc=2)
pylab.savefig('1.png')
#jpeg херово сжимает
# svg, pdf, ips
pylab.show()

#
# import numpy
# l = numpy.zeros(1000)
# for i in range(1000):
#     l[i] = i

init_time = time.perf_counter()
a = []
list_in_measurements = []
n = 100000
m = 1000
for i in range(n):
    if i % m == 0:
        list_measurements.append(time.perf_counter() - init_time)

#pylab.plot(list_measurements)
#pylab.xlabel()
#pylab.show()
#print(list_measurements[-1])
#
#
init_time = time.perf_counter()
a = set()
set_measurements = []
n = 10000
m = 1000
for i in range(n):
    a.add(i)
    if i % m == 0:
        set_measurements.append(time.perf_counter() - init_time)

