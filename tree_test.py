import unittest
from tree import TreeNode


class TestTree(unittest.TestCase):
    def test_add_child(self):
        alice = TreeNode("Alice")
        alice_jr = TreeNode("Alice Jr")
        bob = TreeNode("Bob")
        bob_jr = TreeNode("Bob Jr")
        alice.add_child(alice_jr)
        alice.add_child(bob)
        bob.add_child(bob_jr)
        self.assertEqual(alice.traverse(), "Alice : Bob : Bob Jr : Alice Jr")

    def test_remove_child(self):
        alice = TreeNode("Alice")
        bob = TreeNode("Bob")
        colin = TreeNode("Colin")
        alice.add_child(bob)
        alice.add_child(colin)
        self.assertEqual(alice.traverse(), "Alice : Colin : Bob")
        alice.remove_child(bob)
        self.assertEqual(alice.traverse(), "Alice : Colin")
        alice.remove_child(colin)
        self.assertEqual(alice.traverse(), "Alice")
