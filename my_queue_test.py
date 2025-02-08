import unittest
from my_queue import *


class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())

    def test_has_space(self):
        q = Queue()
        q.enqueue(1)
        self.assertTrue(q.has_space())
        q = Queue(1)
        q.enqueue(1)
        self.assertFalse(q.has_space())

    def test_peek(self):
        q = Queue()
        self.assertIsNone(q.peek())
        q.enqueue(1)
        self.assertEqual(q.peek(), 1)

    def test_dequeue(self):
        q = Queue()
        self.assertIsNone(q.dequeue())
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.get_size(), 0)

    def test_max_size(self):
        max_size = 1
        q = Queue(max_size)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.get_size(), 1)
