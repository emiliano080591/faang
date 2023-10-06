from linked_list.base.node import Node
from linked_list.base.simple_linked_list import SLinkedList


def reverse_linked_list(head: Node) -> SLinkedList:
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return SLinkedList(prev)
