class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        old_head = self.head
        if old_head is not None:
            old_head.set_prev(new_head)
            new_head.set_next(old_head)
        self.head = new_head
        if self.tail is None:
            self.tail = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        old_tail = self.tail
        if old_tail is not None:
            old_tail.set_next(new_tail)
            new_tail.set_prev(old_tail)
        self.tail = new_tail
        if self.head is None:
            self.head = self.tail

    def remove_head(self):
        if self.head is None:
            return None
        if self.head.get_next() is None:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.get_value()
        old_head = self.head
        new_head = old_head.get_next()
        new_head.set_prev(None)
        self.head = new_head
        return old_head.get_value()

    def remove_tail(self):
        if self.tail is None:
            return None
        if self.tail.get_prev() is None:
            old_tail = self.tail
            self.tail = None
            self.head = None
            return old_tail.get_value()
        old_tail = self.tail
        new_tail = self.tail.get_prev()
        new_tail.set_next(None)
        self.tail = new_tail
        return old_tail.get_value()

    def remove_by_value(self, value_to_remove):
        if self.head is None:
            return None
        if self.head.get_value() == value_to_remove:
            old_head = self.head
            self.remove_head()
            return old_head
        if self.tail.get_value() == value_to_remove:
            old_tail = self.tail
            self.remove_tail()
            return old_tail
        # the node to remove is in the middle
        # loop through the middle nodes and if we find it, remove it
        current_node = self.head.get_next()
        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                prev_node = current_node.get_prev()
                next_node = current_node.get_next()
                prev_node.set_next(next_node)
                next_node.set_prev(prev_node)
                return current_node
            current_node = current_node.get_next()
        # return None if didn't find it
        return None

    def stringify_list(self):
        stringified = ""
        node = self.head
        while node is not None:
            stringified += str(node.get_value()) + "\n"
            node = node.get_next()
        return stringified
