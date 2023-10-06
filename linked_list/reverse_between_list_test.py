import unittest

from linked_list.base.node import Node
from linked_list.reverse_between_list_2 import reverse_between
from linked_list.base.simple_linked_list import SLinkedList


class Test(unittest.TestCase):
    def test_reverse_list(self):
        head = generate_test_case().head_val
        self.assertListEqual(reverse_between(head, 2, 5).list_to_array(), [1, 5, 4, 3, 2, 6])


def generate_test_case() -> SLinkedList:
    list = SLinkedList(Node(1))
    list.add_node(Node(2))
    list.add_node(Node(3))
    list.add_node(Node(4))
    list.add_node(Node(5))
    list.add_node(Node(6))

    return list
