import unittest

from linked_list.base.simple_linked_list import SLinkedList
from linked_list.reverse_between_list_2 import reverse_between


class Test(unittest.TestCase):
    def test_reverse_list(self):
        head = generate_test_case().head_val
        self.assertListEqual(reverse_between(head, 2, 5).list_to_array(), [1, 5, 4, 3, 2, 6])


def generate_test_case() -> SLinkedList:
    list = SLinkedList(1)
    list.add_node(2)
    list.add_node(3)
    list.add_node(4)
    list.add_node(5)
    list.add_node(6)

    return list
