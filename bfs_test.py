import unittest
from bfs import breadth_first_search
from tree import TreeNode

class TestBfs(unittest.TestCase):

    def test_bfs(self):
        sample_root_node = TreeNode("Home")
        docs = TreeNode("Documents")
        photos = TreeNode("Photos")
        sample_root_node.children = [docs, photos]
        my_wish = TreeNode("WishList.txt")
        my_todo = TreeNode("TodoList.txt")
        my_cat = TreeNode("Fluffy.jpg")
        my_dog = TreeNode("Spot.jpg")
        docs.children = [my_wish, my_todo]
        photos.children = [my_cat, my_dog]
        self.assertIsNone(breadth_first_search(sample_root_node, "sausage"))
        self.assertEqual(breadth_first_search(sample_root_node, "Fluffy.jpg"), [sample_root_node, photos, my_cat])
