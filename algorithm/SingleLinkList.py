# -*-coding:utf-8-*-


class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None

    def __str__(self):
        return "element = %s" % (self.element)


class SingleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        curr = self.__head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def travel(self):
        """遍历整个链表"""
        curr = self.__head
        while curr is not None:
            print(curr.element, end=" ")
            curr = curr.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            curr = self.__head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = Node(item)
        if pos == 0:
            node.next, self.__head = self.__head, node
        else:
            curr_pre = self.__head
            index = 0
            try:
                while index < pos - 1:
                    index += 1
                    curr_pre = curr_pre.next
                node.next, curr_pre.next = curr_pre.next, node
            except AttributeError:
                print("IndexOutOfPointExceptionX")

    def remove(self, item):
        """删除节点"""
        curr = self.__head
        pre_node = None
        while curr is not None:
            if curr.element == item:
                if not pre_node:
                    self.__head = curr.next
                else:
                    pre_node.next = curr.next
                break
            else:
                pre_node = curr
                curr = curr.next

    def search(self, item):
        """查找节点是否存在"""
        curr = self.__head
        while curr is not None:
            if curr.element == item:
                return True
            curr = curr.next
        return False


if __name__ == "__main__":
    link_list = SingleLinkList()
    print(link_list.is_empty())
    print(link_list.length())

    print("尾部插入节点")
    link_list.append(1)
    print(link_list.is_empty())
    print(link_list.length())
    print(20 * "-")

    print("尾部插入节点")
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)
    link_list.travel()
    print(link_list.length())
    print(20 * "-")

    print("头部插入节点")
    link_list.add(6)
    link_list.travel()
    print(link_list.length())
    print(20 * "-")

    print("指定位置插入节点")
    link_list.insert(1, 7)
    link_list.travel()
    print(link_list.length())
    print(20 * "-")

    print("移除节点")
    link_list.remove(0)
    link_list.travel()
    print(link_list.length())
    print(20 * "-")

    print("查询节点")
    print(link_list.search(9))
    print(20 * "-")


