from linked_list.base.node import NodeDouble


class DLinkedList:
    def __init__(self, node: NodeDouble):
        self.head_val = node

    def print_list(self):
        node = self.head_val
        while node is not None:
            print(node.data)
            node = node.next

    def add_node(self,node:NodeDouble):
        if self.head_val is None:
            new_node = node
            self.head_val = new_node
            return
        n = self.head_val
        while n.next is not None:
            n = n.next
        new_node = node
        n.next = new_node
        new_node.prev = n

    def list_to_array(self) -> []:
        array = []
        node = self.head_val
        while node is not None:
            array.append(node.data)
            node = node.next
        return array
