import unittest
from blossom import Hashmap


class TestBlossom(unittest.TestCase):
    def test_hashmap(self):
        hashmap = Hashmap(1)
        hashmap.assign("Alan", 42)
        hashmap.assign("Bob", 87)
        hashmap.assign("Celine", 22)
        self.assertEqual(hashmap.retrieve("Alan"), 42)
        self.assertEqual(hashmap.retrieve("Celine"), 22)
        self.assertIsNone(hashmap.retrieve("Billie"))
