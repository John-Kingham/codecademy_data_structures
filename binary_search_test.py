import unittest
from binary_search import bsr


class TestBinarySearchRecursive(unittest.TestCase):

    def test_bsr(self):
        sorted_list = [77, 80, 102, 123, 288, 300, 540]
        left_pointer = 0
        right_pointer = len(sorted_list)
        self.assertIsNone(bsr(sorted_list, left_pointer, right_pointer, -1))
        self.assertEqual(bsr(sorted_list, left_pointer, right_pointer, 77), 0)
        self.assertEqual(bsr(sorted_list, left_pointer, right_pointer, 123), 3)
        self.assertEqual(bsr(sorted_list, left_pointer, right_pointer, 540), 6)
        