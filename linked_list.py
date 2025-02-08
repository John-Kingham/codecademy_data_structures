class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_head_node_value):
        new_head_node = Node(new_head_node_value)
        new_head_node.set_next_node(self.head_node)
        self.head_node = new_head_node

    def stringify_list(self):
        values_string = ""
        node = self.head_node
        while node is not None:
            if node.get_value() is not None:
                values_string += str(node.get_value()) + "\n"
            node = node.get_next_node()
        return values_string

    def remove_node(self, value_to_remove):
        if self.head_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()
            return
        current_node = self.head_node
        next_node = current_node.get_next_node()
        while next_node is not None:
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                return
            else:
                current_node = next_node
                next_node = current_node.get_next_node()

    def swap_nodes(self, value1, value2):
        if value1 == value2:
            return "No swap needed - values are identical"
        node1, node1_prev = self.find_node_and_previous(value1)
        node2, node2_prev = self.find_node_and_previous(value2)
        if node1 is None or node2 is None:
            return "Swap not possible - one or more values missing from list"
        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)
        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)
        return None

    def find_node_and_previous(self, value):
        node = self.head_node
        previous_node = None
        while node is not None and node.get_value() != value:
            previous_node = node
            node = node.get_next_node()
        return node, previous_node

    def length(self):
        length = 0
        node = self.head_node
        while node is not None:
            length += 1
            node = node.get_next_node()
        return length

    def nth_last_node(self, n):
        tail = self.head_node
        nth_from_last = None
        counter = 1
        while tail is not None:
            tail = tail.get_next_node()
            counter += 1
            if counter <= n + 1:
                continue
            if nth_from_last == None:
                nth_from_last = self.head_node
            else:
                nth_from_last = nth_from_last.get_next_node()
        return nth_from_last

    def find_middle(self):
        fast = self.head_node
        slow = self.head_node
        while fast is not None:
            fast = fast.get_next_node()
            if fast is not None:
                fast = fast.get_next_node()
                slow = slow.get_next_node()
        return slow
