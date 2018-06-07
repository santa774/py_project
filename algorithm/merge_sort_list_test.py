# -*-coding:utf-8-*-
def merge_sort(alist):
    """归并排序"""
    # 递归结束条件：当返回的列表长度等于1的时候
    if len(alist) <= 1:
        return alist

    # 将列表平分为2个列表，直到列表只剩一个元素，
    mid = len(alist)//2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    # 然后依次对平分出来的每2个列表进行排序，排好序后依次返回给调用函数
    left_index, right_index = 0, 0
    temp_list = []
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            temp_list.append(left_list[left_index])
            left_index += 1
        else:
            temp_list.append(right_list[right_index])
            right_index += 1
    temp_list += left_list[left_index:]
    temp_list += right_list[right_index:]
    return temp_list





def merge_sort2(list):
    """
    # 对半分列表，获得2个列表
    # 对2个列表进行递归调用此方法，知道列表的长度为1
    # 排序规则：创建2个指针，1个用于存放元素比较后的列表，2个指针分别指向获得的2个列表，按照比较顺序放进新建的列表中，并移动这个列表的指针，最后返回这个新建的列表
    """
    if len(list) <= 1:
        return list

    mid = len(list)//2
    left_list = merge_sort2(list[:mid])
    right_list = merge_sort2(list[mid:])
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
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # result_list = merge_sort(li)
    # print(result_list)
    r2 = merge_sort2(li)
    print(r2)

