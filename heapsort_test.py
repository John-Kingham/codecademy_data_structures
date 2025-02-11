import unittest
import random
from heapsort import heapsort, MaxHeap


class TestHeapsort(unittest.TestCase):
    
    def test_heapsort(self):
        reverse_sorted_list = [n for n in range(10, 0, -1)]
        sorted_list = [n for n in range(1, 11)]
        self.assertEqual(heapsort(reverse_sorted_list), sorted_list)
