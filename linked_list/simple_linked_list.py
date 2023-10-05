class SLinkedList:
    def __init__(self, node=None):
        self.head_val = node

    def print_list(self):
        node = self.head_val
        while node is not None:
            print(node.data)
            node = node.next

    def add_node(self, node):
        last_val = self.head_val
        if self.head_val is None:
            self.head_val = node
            return

        while last_val.next is not None:
            last_val = last_val.next

        last_val.next = node

    def list_to_array(self) -> []:
        array = []
        node = self.head_val
        while node is not None:
            array.append(node.data)
            node = node.next
        return array

    def reverse(self):
        prev = None
        current = self.head_val

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return SLinkedList(prev)
