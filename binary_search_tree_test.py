import unittest
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def test_insert_and_traversal(self):
        traversal_string = "D=2,V=50\nD=3,V=100\nD=4,V=150\nD=1,V=175\nD=2,V=200\nD=3,V=250\nD=4,V=300\n"
        root = BinarySearchTree(175)
        for i in (50, 100, 150, 200, 250, 300):
            root.insert(i)
        self.assertEqual(root.depth_first_in_order_traversal(), traversal_string)

    def test_get_node_by_value(self):
        traversal_string = "D=2,V=50\nD=3,V=100\nD=4,V=150\nD=1,V=175\nD=2,V=200\nD=3,V=250\nD=4,V=300\n"
        root = BinarySearchTree(175)
        for i in (50, 100, 150, 200, 250, 300):
            root.insert(i)
        self.assertIsNone(root.get_node_by_value(-1))
        self.assertEqual(root.get_node_by_value(50).value, 50)
