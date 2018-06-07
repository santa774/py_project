# -*-coding:utf-8
from timeit import Timer


def t1():
    li = []
    for i in range(1000):
        li += [i]


def t2():
    li = [i for i in range(1000)]


def t3():
    li = []
    for i in range(1000):
        li.append(i)


def t4():
    li = list(range(1000))
    

time1 = Timer("t1()", "from __main__ import t1")
print("+:", time1.timeit(1000))
time2 = Timer("t2()", "from __main__ import t2")
print("li = [i for i in range(1000)]:", time2.timeit(1000))
time3 = Timer("t3()", "from __main__ import t3")
print("append:", time3.timeit(1000))
time4 = Timer("t4()", "from __main__ import t4")
print("list:", time4.timeit(1000))
