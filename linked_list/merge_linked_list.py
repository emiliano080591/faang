from linked_list.base.double_linked_list import DLinkedList
from linked_list.base.node import NodeDouble


def flatten(head: NodeDouble) -> DLinkedList:
    if head is None:
        return head

    current_node = head
    while current_node is not None:
        if current_node.child is None:
            current_node = current_node.next
        else:
            tail = current_node.child

            while tail.next is not None:
                tail = tail.next

            tail.next = current_node.next
            if tail.next is not None:
                tail.next.prev = tail
            current_node.next = current_node.child
            current_node.next.prev = current_node
            current_node.child = None

    return DLinkedList(head)
