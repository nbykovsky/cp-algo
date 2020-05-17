import random

import pytest
from lib.avl_tree import AvlTree


def verify(node):
    lh = node.left.height if node.left else 0
    rh = node.right.height if node.right else 0
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


def verify_num(node):
    if node.num_left != (node.left.num_total if node.left else 0) + 1:
        raise Exception("Wrong num left %s " % node.num_left)
    if (
        node.num_total
        != (node.left.num_total if node.left else 0)
        + (node.right.num_total if node.right else 0)
        + 1
    ):
        raise Exception("Wrong num total %s" % node.num_total)
    if node.left:
        verify_num(node.left)
    if node.right:
        verify_num(node.right)


def test_get_from_empty():
    avl = AvlTree()
    assert avl.get(5) == -1


def test_add_element():
    avl = AvlTree()
    avl.add(1, 2)
    assert avl.get(1) == 2
    assert avl._tree.height == 1


def test_add_2elements():
    avl = AvlTree()
    avl.add(1, 2)
    avl.add(2, 3)
    assert avl._tree.height == 2


def test_add_3elements():
    avl = AvlTree()
    avl.add(1, 2)
    avl.add(2, 3)
    avl.add(3, 4)
    assert avl._tree.height == 2


def test_add_4elements():
    avl = AvlTree()
    avl.add(1, 2)
    avl.add(2, 3)
    avl.add(3, 4)
    avl.add(4, 5)
    assert avl._tree.height == 3


def test_add_several():
    avl = AvlTree()
    n = 10
    for i in range(n):
        avl.add(i, i * 100)
    for i in range(n):
        assert avl.get(i) == i * 100


def test_remove_one():
    avl = AvlTree()
    avl.add(1, 2)
    avl.remove(1)
    assert avl._tree is None


def test_remove_two():
    avl = AvlTree()
    avl.add(1, 2)
    avl.add(2, 3)
    avl.remove(1)
    assert avl.get(1) == -1
    avl.remove(2)
    assert avl.get(2) == -1
    assert avl._tree is None


def test_correct_parent():
    avl = AvlTree()
    n = 6
    for i in range(n):
        avl.add(i, i * 100)
    assert avl._tree.left.right.key == 2
    assert avl._tree.left.right.parent.key == 1


def test_remove_6():
    avl = AvlTree()
    n = 6
    for i in range(n):
        avl.add(i, i * 100)
    avl.remove(1)
    assert avl.get(1) == -1
    assert avl.get(2) == 200


def test_remove_many():
    avl = AvlTree()
    n = 100
    for i in range(n):
        avl.add(i, i * 100)
    for i in range(1, n, 2):
        avl.remove(i)
    for i in range(0, n, 2):
        assert avl.get(i) == i * 100
    for i in range(1, n, 2):
        assert avl.get(i) == -1


def test_height():
    avl = AvlTree()
    avl.add(74, 1)
    avl.add(5, 2)
    avl.add(55, 3)
    assert avl._tree.height == 2
    assert avl._tree.left.height == 1


def test_check_invariants():
    s = set()
    avl = AvlTree()
    random.seed(10)
    for _ in range(3):
        x = random.randint(1, 100)
        if x in s:
            assert avl.get(x) == x * 13
            avl.remove(x)
            assert avl.get(x) == -1
            s.remove(x)
        else:
            assert avl.get(x) == -1
            avl.add(x, x * 13)
            assert avl.get(x) == x * 13
            s.add(x)
        verify(avl._tree)


def test_check_invariants_nums():
    avl = AvlTree()
    random.seed(1000)
    for _ in range(3):
        x = random.randint(1, 100)
        avl.add(x, x * 13)
        verify_num(avl._tree)


def test_get_at():
    avl = AvlTree()
    avl.add(1, 1)
    avl.add(10, 10)
    avl.add(5, 5)
    avl.add(3, 3)
    avl.add(7, 7)
    assert avl.get_at(0) == (1, 1)
    assert avl.get_at(1) == (3, 3)
    assert avl.get_at(2) == (5, 5)
    assert avl.get_at(3) == (7, 7)
    assert avl.get_at(4) == (10, 10)
    with pytest.raises(IndexError):
        avl.get_at(-1)
    with pytest.raises(IndexError):
        avl.get_at(5)
    avl.remove(5)
    assert avl.get_at(0) == (1, 1)
    assert avl.get_at(1) == (3, 3)
    assert avl.get_at(2) == (7, 7)
    assert avl.get_at(3) == (10, 10)


def test_num_total():
    avl = AvlTree()
    avl.add(5, 5)
    assert avl._tree.num_total == 1
    assert avl._tree.num_left == 1
    avl.add(2, 2)
    assert avl._tree.num_total == 2
    assert avl._tree.num_left == 2
    assert avl._tree.left.num_total == 1
    assert avl._tree.left.num_left == 1
    avl.add(0, 0)
    assert avl._tree.num_total == 3
    assert avl._tree.num_left == 2
    assert avl._tree.right.num_left == 1
    assert avl._tree.right.num_total == 1
    assert avl._tree.left.num_left == 1
    assert avl._tree.left.num_total == 1
    avl.add(1, 1)
    verify_num(avl._tree)


def test_num_total1():
    avl = AvlTree()
    avl.add(74, 1)
    avl.add(5, 2)
    avl.add(55, 3)

    assert avl._tree.num_total == 3
    assert avl._tree.num_left == 2
    assert avl._tree.right.num_left == 1
    assert avl._tree.right.num_total == 1
    assert avl._tree.left.num_left == 1
    assert avl._tree.left.num_total == 1
