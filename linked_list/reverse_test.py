import unittest

from linked_list.node import Node
from linked_list.reverse import reverse_linked_list
from linked_list.simple_linked_list import SLinkedList


class Test(unittest.TestCase):
    def test_reverse_list(self):
        head = generate_test_case().head_val
        self.assertListEqual(reverse_linked_list(head).list_to_array(), ["Wen", "Tue", "Mon"])
        head = generate_test_case2().head_val
        self.assertListEqual(reverse_linked_list(head).list_to_array(), [5, 4, 3, 2, 1])


def generate_test_case() -> SLinkedList:
    list = SLinkedList(Node("Mon"))
    list.add_node(Node("Tue"))
    list.add_node(Node("Wen"))

    return list


def generate_test_case2() -> SLinkedList:
    list = SLinkedList(Node(1))
    list.add_node(Node(2))
    list.add_node(Node(3))
    list.add_node(Node(4))
    list.add_node(Node(5))

    return list


if __name__ == '__main__':
    unittest.main()
