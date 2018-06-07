# -*-coding:utf-8-*-
def quick_sort(sort_list, start, end):
    """快速排序"""
    # 递归结束条件
    if start >= end:
        return

    # 设定列表的第一个元素为基准值
    mid = sort_list[start]

    # low: 低位分区的指针
    low = start

    # high: 高位分区的指针
    high = end

    while low < high:
        # high指针 从右往左将小于基准值的元素移动到 low指针所指的位置
        # 计算high指针的位置
        while low < high and sort_list[high] > mid:
            high -= 1
        sort_list[low] = sort_list[high]

        # low指针 从左往右移动将大于基准值的元素移动到 high指针所指的位置
        # 计算low指针的位置
        while low < high and sort_list[low] < mid:
            low += 1
        sort_list[high] = sort_list[low]

    # 当low和high重合后，将low指针赋值为基准值
    sort_list[low] = mid

    # 递归调用，将小于基准值的列表排序
    quick_sort(sort_list, start, low - 1)
    # 递归调用，将大于基准值的列表排序
    quick_sort(sort_list, low + 1, end)


























def quick_sort2(list, start, end):
    # 设定基准值mid
    # 将小于基准值的放在mid左边，大于基准值的放在mid右边
    # 需要2个指针，low， high，当两个指针没有重合的时候，把high指针指向的值与mid比较，如果小于mid，则把此值赋值给low指针所指的位置，并将high指针-1
    # 把low指针指向的值与mid比较，如果大于mid，则把此值赋值给high指针所指的位置，并将low指针+1、
    # 当一个循环走下来后，mid左边的都是小于它的，mid右边的都是大于它的，然后再将2组独立的列表进行快排（即递归调用，结束的条件是low>=high的时候）
    if start >= end:
        return

    low = start
    high = end
    mid = list[start]

    while low < high:
        while low < high and list[high] > mid:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] < mid:
            low += 1
        list[high] = list[low]

    list[low] = mid

    quick_sort2(list, start, low - 1)
    quick_sort2(list, low + 1, end)
























if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(li, 0, len(li)-1)
    quick_sort2(li, 0, len(li) - 1)
    print(li)

