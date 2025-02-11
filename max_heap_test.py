import unittest
from max_heap import MaxHeap


class TestMaxHeap(unittest.TestCase):

    def test_max_heap(self):
        test_list = [n for n in range(1, 11)]
        heapified_list = [None, 10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
        max_heap = MaxHeap()
        for n in test_list:
            max_heap.add(n)
        self.assertEqual(max_heap.heap_list, heapified_list)
        