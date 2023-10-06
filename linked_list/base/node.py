class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class NodeDouble:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
