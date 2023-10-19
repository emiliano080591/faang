from linked_list.base.node import Node


def find_cycle(head: Node) -> Node:
    if head is None:
        return head

    tortoise = head
    hare = head

    while True:
        tortoise = tortoise.next
        hare = hare.next

        if hare is None or hare.next is None:
            return None
        else:
            hare = hare.next
        if tortoise == hare:
            break

    p1 = head
    p2 = tortoise

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p2
