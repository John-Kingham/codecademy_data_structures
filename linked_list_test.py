import unittest
from linked_list import *


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList(3)
        for i in range(2, 0, -1):
            self.ll.insert_beginning(i)

    def tearDown(self):
        self.ll = None

    def test_node_linking(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.set_next_node(node2)
        self.assertEqual(node1.get_next_node(), node2)

    def test_new_linked_list(self):
        self.assertEqual(self.ll.get_head_node().get_value(), 1)

    def test_insert_beginning(self):
        self.ll.insert_beginning(5)
        self.assertEqual(self.ll.get_head_node().get_value(), 5)

    def test_stringify_list(self):
        self.assertEqual(self.ll.stringify_list(), "1\n2\n3\n")

    def test_remove_node(self):
        self.ll.remove_node(2)
        self.assertEqual(self.ll.get_head_node().get_next_node().get_value(), 3)

    def test_swap_nodes(self):
        message = self.ll.swap_nodes(1, 2)
        self.assertEqual(self.ll.stringify_list(), "2\n1\n3\n")
        self.assertEqual(message, None)
        message = self.ll.swap_nodes(1, 1)
        self.assertEqual(message, "No swap needed - values are identical")
        message = self.ll.swap_nodes(10, 1)
        self.assertEqual(
            message, "Swap not possible - one or more values missing from list"
        )

    def test_length(self):
        self.assertEqual(self.ll.length(), 3)

    def test_nth_last_node(self):
        self.assertEqual(self.ll.nth_last_node(1).get_value(), 2)

    def test_find_middle(self):
        self.assertEqual(self.ll.find_middle().get_value(), 2)


if __name__ == "__main__":
    unittest.main()
