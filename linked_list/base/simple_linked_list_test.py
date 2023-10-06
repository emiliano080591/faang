from linked_list.base.node import Node
from linked_list.base.simple_linked_list import SLinkedList

if __name__ == '__main__':
    list = SLinkedList(Node("Mon"))
    list.add_node(Node("Tue"))
    list.add_node(Node("Wen"))

    list.print_list()
