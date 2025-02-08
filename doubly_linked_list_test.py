import unittest
from doubly_linked_list import *


class TestDoublyLinkedList(unittest.TestCase):

    def test_new_node(self):
        value, next_value, prev_value = 2, 3, 1
        node = Node(value, Node(next_value), Node(prev_value))
        self.assertEqual(node.get_value(), value)
        self.assertEqual(node.get_next().get_value(), next_value)
        self.assertEqual(node.get_prev().get_value(), prev_value)

    def test_add_to_head(self):
        dll = DoublyLinkedList()
        dll.add_to_head(3)
        dll.add_to_head(2)
        dll.add_to_head(1)
        self.assertEqual(dll.head.get_value(), 1)

    def test_add_to_tail(self):
        dll = DoublyLinkedList()
        dll.add_to_tail(1)
        self.assertEqual(dll.get_tail().get_value(), 1)
        self.assertEqual(dll.get_head().get_value(), 1)
        dll.add_to_tail(2)
        self.assertEqual(dll.get_tail().get_value(), 2)
        self.assertEqual(dll.get_head().get_value(), 1)

    def test_remove_head(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.remove_head(), None)
        dll.add_to_head(1)
        self.assertEqual(dll.remove_head(), 1)
        self.assertEqual(dll.remove_head(), None)
        for i in range(3):
            dll.add_to_tail(i + 1)
        self.assertEqual(dll.remove_head(), 1)
        self.assertEqual(dll.remove_head(), 2)
        self.assertEqual(dll.remove_head(), 3)
        self.assertEqual(dll.remove_head(), None)

    def test_remove_tail(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.remove_tail(), None)
        dll.add_to_head(1)
        self.assertEqual(dll.remove_tail(), 1)
        for i in range(3):
            dll.add_to_tail(i + 1)
        self.assertEqual(dll.remove_tail(), 3)
        self.assertEqual(dll.remove_tail(), 2)
        self.assertEqual(dll.remove_tail(), 1)
        self.assertEqual(dll.remove_tail(), None)

    def test_remove_by_value(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.remove_by_value(1), None)
        dll.add_to_head(1)
        self.assertEqual(dll.remove_by_value(1).get_value(), 1)
        self.assertEqual(dll.get_head(), None)
        for i in range(5):
            dll.add_to_tail(i + 1)
        # test removing the head by value
        self.assertEqual(dll.remove_by_value(1).get_value(), 1)
        self.assertEqual(dll.remove_by_value(1), None)
        # test removing a middle node by value
        self.assertEqual(dll.remove_by_value(3).get_value(), 3)
        self.assertEqual(dll.remove_by_value(3), None)
        # test removing the tail by value
        self.assertEqual(dll.remove_by_value(5).get_value(), 5)
        self.assertEqual(dll.remove_by_value(5), None)
        # test that other nodes weren't removed
        self.assertEqual(dll.get_head().get_value(), 2)

    def test_stringify_list(self):
        dll = DoublyLinkedList()
        for i in range(4):
            dll.add_to_tail(i + 1)
        self.assertEqual(dll.stringify_list(), "1\n2\n3\n4\n")


if __name__ == "__main__":
    unittest.main()
