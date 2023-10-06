from linked_list.base.node import NodeDouble


class DLinkedList:
    def __init__(self, node=None):
        self.head_val = node

    def add_node(self, data=None):
        if self.head_val is None:
            new_node = NodeDouble(data)
            self.head_val = new_node
            return
        n = self.head_val
        while n.next is not None:
            n = n.next
        new_node = NodeDouble(data)
        n.next = new_node
        new_node.prev = n