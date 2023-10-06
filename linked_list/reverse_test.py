import unittest

from linked_list.base.node import Node
from linked_list.base.simple_linked_list import SLinkedList


class Test(unittest.TestCase):
    def test_reverse_list(self):
        self.assertListEqual(generate_test_case().reverse().list_to_array(), ["Wen", "Tue", "Mon"])
        head = generate_test_case2().head_val
        self.assertListEqual(generate_test_case2().reverse().list_to_array(), [5, 4, 3, 2, 1])


def generate_test_case() -> SLinkedList:
    list = SLinkedList("Mon")
    list.add_node("Tue")
    list.add_node("Wen")

    return list


def generate_test_case2() -> SLinkedList:
    list = SLinkedList(1)
    list.add_node(2)
    list.add_node(3)
    list.add_node(4)
    list.add_node(5)

    return list


if __name__ == '__main__':
    unittest.main()
