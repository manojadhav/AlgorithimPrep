class doulylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def containsnodewithvalue (self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None