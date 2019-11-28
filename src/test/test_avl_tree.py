import unittest
from src.main.avl_tree import AvlTree

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