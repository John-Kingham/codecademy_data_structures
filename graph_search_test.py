import unittest
from graph_search import dfs, bfs


class TestGraphSearch(unittest.TestCase):

    def setUp(self):
        # Sets are unordered, so the order of items in a set isn't reliable.
        # This is bad for testing, which requires consistency.
        # To avoid this, the test graph uses lists instead of sets.
        self.graph = {
            "lava": ["sharks", "piranhas"],
            "sharks": ["piranhas", "bees"],
            "piranhas": ["bees"],
            "bees": ["lasers"],
            "lasers": [],
        }

    def test_dfs(self):
        self.assertEqual(
            dfs(self.graph, "lava", "bees"), ["lava", "sharks", "piranhas", "bees"]
        )
        self.assertEqual(dfs(self.graph, "bees", "lasers"), ["bees", "lasers"])
        self.assertIsNone(dfs(self.graph, "bees", "not in graph"))

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, "lava", "bees"), ["lava", "sharks", "bees"])
        self.assertIsNone(bfs(self.graph, "sharks", "not in graph"))
