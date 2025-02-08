import unittest
from hashmap import HashMap


class TestHashmap(unittest.TestCase):

    def test_assign(self):
        hash_map = HashMap(3)
        hash_map.assign("Anne", 53)
        hash_map.assign("Bob", 50)
        hash_map.assign("Colin", 17)
        self.assertEqual(hash_map.retrieve("Bob"), 50)
        HASH_FULL = 1
        self.assertEqual(hash_map.assign("Eliza", 67), HASH_FULL)

    def test_retrieve(self):
        hash_map = HashMap(3)
        hash_map.assign("Anne", 53)
        hash_map.assign("Bob", 50)
        hash_map.assign("Colin", 17)
        self.assertEqual(hash_map.retrieve("Anne"), 53)
        self.assertIsNone(hash_map.retrieve("Dave"))
