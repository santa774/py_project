# -*-coding:utf-8-*-
class Node(object):
    def __init__(self, item=None):
        self.elem = item
        self.l_child = None
        self.r_child = None


class Tree(object):
    def __init__(self):
        self.root = None
        pass

    def add(self, item):
        """添加元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.l_child is None:
                curr_node.l_child = node
                return
            else:
                queue.append(curr_node.l_child)

            if curr_node.r_child is None:
                curr_node.r_child = node
                return
            else:
                queue.append(curr_node.r_child)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return

        queue = [self.root]
        print(self.root.elem, end=" ")
        while queue:
            curr_node = queue.pop(0)
            if curr_node.l_child is not None:
                print(curr_node.l_child.elem, end=" ")
                queue.append(curr_node.l_child)

            if curr_node.r_child is not None:
                print(curr_node.r_child.elem, end=" ")
                queue.append(curr_node.r_child)
        print("")

    def preorder_travel(self, node):
        """深度遍历--先序遍历（根→左→右）"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder_travel(node.l_child)
        self.preorder_travel(node.r_child)

    def midorder_travel(self, node):
        """深度遍历--中序遍历（左→根→右）"""
        if node is None:
            return
        self.midorder_travel(node.l_child)
        print(node.elem, end=" ")
        self.midorder_travel(node.r_child)

    def behindorder_travel(self, node):
        """深度遍历--后序遍历（左→右→根）"""
        if node is None:
            return
        self.behindorder_travel(node.l_child)
        self.behindorder_travel(node.r_child)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.breadth_travel()
    tree.preorder_travel(tree.root)
    print("")
    tree.midorder_travel(tree.root)
    print("")
    tree.behindorder_travel(tree.root)
    print("")
