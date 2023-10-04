from linked_list.node import Node
from linked_list.simple_linked_list import SLinkedList

if __name__ == '__main__':
    list = SLinkedList(Node("Mon"))
    list.add_node(Node("Tue"))
    list.add_node(Node("Wen"))

    list.print_list()
