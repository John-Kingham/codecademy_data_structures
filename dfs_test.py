import unittest
from tree import TreeNode
from dfs import dfs


class DfsTest(unittest.TestCase):

    def test_dfs(self):
        root_node_value = "A"
        root = TreeNode(root_node_value)
        root_path = (root,)
        two = TreeNode("B")
        three = TreeNode("C")
        root.children = [three, two]
        four = TreeNode("D")
        five = TreeNode("E")
        six_node_value = "F"
        six = TreeNode(six_node_value)
        six_path = (root, three, six)
        seven = TreeNode("G")
        two.children = [five, four]
        three.children = [seven, six]
        self.assertIsNone(dfs(root, "not in tree"))
        self.assertEqual(dfs(root, root_node_value), root_path)
        self.assertEqual(dfs(root, six_node_value), six_path)
