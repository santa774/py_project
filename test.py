# -*-coding:utf-8-*-
import time
from timeit import Timer


class TestGetAttr(object):
    def __getattr__(self, item):
        print(item, end=" ")
        return self

    def __str__(self):
        return ""


test = TestGetAttr()
print(test.hello.world.test)


def test1():
    """
    如果a+b+c=1000，且a^2+b^2=c^2（a，b，c为自然数），如何求出所有a，b，c的组合？
    :return:
    """
    start_time = time.time()
    for a in range(0, 1000):
        for b in range(0, 1000):
            for c in range(0, 1000):
                if (a + b + c == 1000) & (a * a + b * b == c * c):
                    print("a=%s, b=%s, c=%s" % (a, b, c))

    end_time = time.time() - start_time
    print("耗时：%s" % end_time)


def test2():
    """
    如果a+b+c=1000，且a^2+b^2=c^2（a，b，c为自然数），如何求出所有a，b，c的组合？
    :return:
    """
    start_time = time.time()
    for a in range(0, 1000):
        for b in range(0, 1000):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print("a=%s, b=%s, c=%s" % (a, b, c))

    end_time = time.time() - start_time
    print("耗时：%s" % end_time)


# # t1 = Timer(test1(), "from __main__ import test1")
# # print("test1():", t1.timer(1000))
# t2 = Timer("test2()", "from __main__ import test2")
# print("test2():", t2.timeit(2) / 2)





def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list)//2
    left_list = merge_sort(list[:mid])
    right_list = merge_sort(list[mid:])

    left_index, right_index = 0, 0
    sorted_list = []
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1
    sorted_list += left_list[left_index:]
    sorted_list += right_list[right_index:]
    return sorted_list


if __name__ == "__main__":
    li = [22, 55, 11, 99, 44, 88, 00]
    li2 = merge_sort(li)
    print(li2)




