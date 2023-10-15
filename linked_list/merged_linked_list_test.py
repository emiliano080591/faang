import unittest

from linked_list.base.double_linked_list import DLinkedList
from linked_list.base.node import NodeDouble
from linked_list.merge_linked_list import flatten


class Test(unittest.TestCase):
    def test_flatten_list(self):
        list = generate_test_case()
        list = flatten(list.head_val)
        self.assertListEqual(list.list_to_array(), [1, 2, 7, 8, 9, 3, 4, 5, 6])


def generate_test_case() -> DLinkedList:
    sub_list = DLinkedList(NodeDouble(data=7))
    sub_list.add_node(NodeDouble(data=8))
    sub_list.add_node(NodeDouble(data=9))

    list = DLinkedList(NodeDouble(data=1))
    list.add_node(NodeDouble(data=2, child=sub_list.head_val))
    list.add_node(NodeDouble(data=3))
    list.add_node(NodeDouble(data=4))
    list.add_node(NodeDouble(data=5))
    list.add_node(NodeDouble(data=6))

    return list
