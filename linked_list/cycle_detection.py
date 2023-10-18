from linked_list.base.node import Node


def find_cycle(head: Node) -> Node:
    current_node = head
    seen_nodes = set()

    while not (current_node in seen_nodes):
        if current_node.next is None:
            return None
        seen_nodes.add(current_node)
        current_node = current_node.next
    return current_node
