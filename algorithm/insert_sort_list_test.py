# -*-coding:utf-8-*-


def insert_sort(sort_list):
    """插入排序"""
    for i in range(1, len(sort_list)):
        for j in range(i, 0, -1):
            if sort_list[j] < sort_list[j - 1]:
                sort_list[j], sort_list[j - 1] = sort_list[j - 1], sort_list[j]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(li)
    print(li)

    # for i in range(len(li)-1, -1, -1):
    #     print(li[i], end=" ")

