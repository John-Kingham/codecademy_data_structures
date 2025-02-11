import unittest
from heap_map import HeapMap


class TestHeapMap(unittest.TestCase):

    def test_heap_map(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        heapified_list = [None, 10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
        heap_map = HeapMap()
        for n in test_list:
            heap_map.add(n)
        self.assertEqual(heap_map.heap_list, heapified_list)
        