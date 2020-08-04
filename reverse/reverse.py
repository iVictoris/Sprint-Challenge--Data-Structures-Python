class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.queue = []

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def add_to_queue(self, value):
        # adds to front of queue list
        self.queue = [value] + self.queue

    def remove_from_queue(self):
        # removes from front of queue
        poppped = self.queue[len(self.queue)-1]
        self.queue = self.queue[:len(self.queue)-1]
        return poppped

    def create_reverse_list(self):
        if len(self.queue) == 0:
            return
        value = self.remove_from_queue()
        self.add_to_head(value)
        self.create_reverse_list()

    def reverse_list(self, node):
        if node is None:
            self.head = None
            self.create_reverse_list()
            return
        self.add_to_queue(node.get_value())
        self.reverse_list(node.get_next())

# finish sprint 5p EST 7/16/2020



        
