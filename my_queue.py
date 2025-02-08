from linked_list import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def has_space(self):
        if self.max_size is None:
            return True
        else:
            return self.get_size() < self.max_size

    def peek(self):
        if self.is_empty():
            print("Nothing to see here!")
            return None
        else:
            return self.head.get_value()

    def enqueue(self, value):
        if self.has_space():
            new_tail = Node(value)
            print(f"Adding {str(value)} to the queue!")
            if self.is_empty():
                self.head = new_tail
                self.tail = new_tail
            else:
                self.tail.set_next_node(new_tail)
                self.tail = new_tail
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        if self.is_empty():
            print("This queue is totally empty!")
            return None
        item_to_remove = self.head
        print(f"Removing {str(item_to_remove.get_value())} from the queue!")
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next_node()
        self.size -= 1
        return item_to_remove.get_value()
