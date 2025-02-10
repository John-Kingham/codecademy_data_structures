import unittest
from binary_search import binary_search_recursive, binary_search_iterative


class TestBinarySearchRecursive(unittest.TestCase):

    def test_binary_search_recursive(self):
        sorted_list = [77, 80, 102, 123, 288, 300, 540]
        left_pointer = 0
        right_pointer = len(sorted_list)
        self.assertIsNone(binary_search_recursive(sorted_list, left_pointer, right_pointer, -1))
        self.assertEqual(binary_search_recursive(sorted_list, left_pointer, right_pointer, 77), 0)
        self.assertEqual(binary_search_recursive(sorted_list, left_pointer, right_pointer, 123), 3)
        self.assertEqual(binary_search_recursive(sorted_list, left_pointer, right_pointer, 540), 6)

    def test_binary_search_iterative(self):
        sorted_list = [77, 80, 102, 123, 288, 300, 540]
        self.assertIsNone(binary_search_iterative(sorted_list, -1))
        self.assertEqual(binary_search_iterative(sorted_list, 77), 0)
        self.assertEqual(binary_search_iterative(sorted_list, 123), 3)
        self.assertEqual(binary_search_iterative(sorted_list, 540), 6)
