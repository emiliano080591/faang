from linked_list.node import Node
from linked_list.simple_linked_list import SLinkedList


def reverse_between(head: Node, m: int, n: int) -> SLinkedList:
    current_pos = 1
    current_node = head
    start = head

    while current_pos < m:
        start = current_node
        current_node = current_node.next
        current_pos += 1

    prev = None
    tail = current_node

    while m <= current_pos <= n:
        next = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next
        current_pos += 1

    start.next = prev
    tail.next = current_node

    if m > 1:
        return SLinkedList(head)
    else:
        return SLinkedList(prev)
