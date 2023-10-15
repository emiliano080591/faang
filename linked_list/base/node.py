class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class NodeDouble:
    def __init__(self, data=None, child=None):
        self.data = data
        self.prev = None
        self.next = None
        self.child = child

    def get_data(self):
        return self.data
