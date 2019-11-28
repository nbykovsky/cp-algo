import unittest
from src.main.avl_tree import AvlTree
import random


def verify(node):
    lh = (node.left.height if node.left else 0)
    rh = (node.right.height if node.right else 0)
    balance_factor = lh - rh
    h = max(lh, rh) + 1
    if balance_factor < -1 or balance_factor > 1:
        raise Exception("Bad balance_factor %s" % balance_factor)
    if node.height != h:
        raise Exception("Wrong height %s (should be %s)" % (node.height, h))
    if node.left:
        verify(node.left)
    if node.right:
        verify(node.right)


class TestAvlTree(unittest.TestCase):

    def test_get_from_empty(self):
        avl = AvlTree()
        self.assertEqual(avl.get(5), -1)

    def test_add_element(self):
        avl = AvlTree()
        avl.add(1,2)
        self.assertEqual(avl.get(1), 2)
        self.assertEqual(avl._tree.height, 1)

    def test_add_2elements(self):
        avl = AvlTree()
        avl.add(1,2)
        avl.add(2,3)
        self.assertEqual(avl._tree.height, 2)

    def test_add_3elements(self):
        avl = AvlTree()
        avl.add(1,2)
        avl.add(2,3)
        avl.add(3,4)
        self.assertEqual(avl._tree.height, 2)

    def test_add_4elements(self):
        avl = AvlTree()
        avl.add(1,2)
        avl.add(2,3)
        avl.add(3,4)
        avl.add(4,5)
        self.assertEqual(avl._tree.height, 3)

    def test_add_several(self):
        avl = AvlTree()
        n = 10
        for i in range(n):
            avl.add(i, i * 100)
        for i in range(n):
            self.assertEqual(avl.get(i), i * 100)

    def test_remove_one(self):
        avl = AvlTree()
        avl.add(1, 2)
        avl.remove(1)
        self.assertTrue(avl._tree is None)

    def test_remove_two(self):
        avl = AvlTree()
        avl.add(1, 2)
        avl.add(2, 3)
        avl.remove(1)
        self.assertTrue(avl.get(1) == -1)
        avl.remove(2)
        self.assertTrue(avl.get(2) == -1)
        self.assertTrue(avl._tree is None)

    def test_correct_parent(self):
        avl = AvlTree()
        n = 6
        for i in range(n):
            avl.add(i, i * 100)
        self.assertTrue(avl._tree.left.right.key == 2)
        self.assertTrue(avl._tree.left.right.parent.key == 1)

    def test_remove_6(self):
        avl = AvlTree()
        n = 6
        for i in range(n):
            avl.add(i, i * 100)
        avl.remove(1)
        self.assertTrue(avl.get(1) == -1)
        self.assertTrue(avl.get(2) == 200)

    def test_remove_many(self):
        avl = AvlTree()
        n = 100
        for i in range(n):
            avl.add(i, i * 100)
        for i in range(1, n, 2):
            avl.remove(i)
        for i in range(0, n, 2):
            self.assertEqual(avl.get(i), i * 100)
        for i in range(1, n, 2):
            self.assertEqual(avl.get(i), -1)

    def test_height(self):
        avl = AvlTree()
        avl.add(74, 1)
        avl.add(5, 2)
        avl.add(55, 3)
        self.assertTrue(avl._tree.height == 2)
        self.assertTrue(avl._tree.left.height == 1)

    def test_check_invariants(self):
        s = set()
        avl = AvlTree()
        random.seed(10)
        for _ in range(10000):
            x = random.randint(1, 100)
            if x in s:
                self.assertTrue(avl.get(x) == x * 13)
                avl.remove(x)
                self.assertTrue(avl.get(x) == -1)
                s.remove(x)
            else:
                self.assertTrue(avl.get(x) == -1)
                avl.add(x, x * 13)
                self.assertTrue(avl.get(x) == x * 13)
                s.add(x)
            verify(avl._tree)

