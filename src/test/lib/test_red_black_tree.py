import random

from lib.red_black_tree import RedBlackTree, Node


def in_order(tree):
    def helper(node):
        if not node:
            return []
        return helper(node.left) + [(node.key, node.color)] + helper(node.right)

    return helper(tree)


def check_invariants(tree):
    # 1. Root must be black
    assert tree.color == Node.BLACK
    number_blacks = set()

    def helper(node, acc):
        nonlocal number_blacks
        if not node:
            number_blacks.add(acc)
            return
        # 2. If a node is red, all of its children must be black
        if node.color == Node.RED:
            assert not node.left or node.left.color == Node.BLACK
            assert not node.right or node.right.color == Node.BLACK

        if node.color == Node.BLACK:
            acc += 1

        helper(node.left, acc)
        helper(node.right, acc)

    helper(tree, 0)
    # 3. For any given node u, every possible path from u to a "null reference"
    #  must contain the same number of black nodes
    assert len(number_blacks) == 1


def test_add_and_get_one_key():
    rbt = RedBlackTree()
    rbt.add(5, 10)
    check_invariants(rbt._tree)
    assert rbt.get(5) == 10
    assert rbt._tree.color == Node.BLACK


def test_state_after_adding_2_values():
    rbt = RedBlackTree()
    rbt.add(5, 10)
    rbt.add(10, 20)
    check_invariants(rbt._tree)
    assert rbt._tree.key == 5
    assert rbt._tree.color == Node.BLACK
    assert rbt._tree.right.key == 10
    assert rbt._tree.right.color == Node.RED


def test_state_after_adding_3_values_asc():
    rbt = RedBlackTree()
    rbt.add(3, 10)
    rbt.add(4, 40)
    rbt.add(5, 50)
    check_invariants(rbt._tree)
    assert rbt._tree.key == 4
    assert rbt._tree.color == Node.BLACK
    assert rbt._tree.right.key == 5
    assert rbt._tree.right.color == Node.RED
    assert rbt._tree.left.key == 3
    assert rbt._tree.left.color == Node.RED


def test_state_after_adding_3_values_desc():
    rbt = RedBlackTree()
    rbt.add(5, 50)
    rbt.add(4, 40)
    rbt.add(3, 10)
    check_invariants(rbt._tree)
    assert rbt._tree.key == 4
    assert rbt._tree.color == Node.BLACK
    assert rbt._tree.right.key == 5
    assert rbt._tree.right.color == Node.RED
    assert rbt._tree.left.key == 3
    assert rbt._tree.left.color == Node.RED


def test_add_6_values():
    rbt = RedBlackTree()
    rbt.add(10, None)
    rbt.add(6, None)
    rbt.add(8, None)
    check_invariants(rbt._tree)
    assert (rbt._tree.left.key, rbt._tree.key, rbt._tree.right.key) == (6, 8, 10)
    assert (rbt._tree.left.color, rbt._tree.color, rbt._tree.right.color) == (
        Node.RED,
        Node.BLACK,
        Node.RED,
    )
    rbt.add(4, None)
    check_invariants(rbt._tree)
    assert (
        rbt._tree.left.left.key,
        rbt._tree.left.key,
        rbt._tree.key,
        rbt._tree.right.key,
    ) == (4, 6, 8, 10)
    assert (
        rbt._tree.left.left.color,
        rbt._tree.left.color,
        rbt._tree.color,
        rbt._tree.right.color,
    ) == (Node.RED, Node.BLACK, Node.BLACK, Node.BLACK)
    rbt.add(7, None)
    rbt.add(6.5, None)
    check_invariants(rbt._tree)
    assert in_order(rbt._tree) == [
        (4, Node.BLACK),
        (6, Node.RED),
        (6.5, Node.RED),
        (7, Node.BLACK),
        (8, Node.BLACK),
        (10, Node.BLACK),
    ]


def test_random_sequence():
    random.seed(100)
    rbt = RedBlackTree()
    generated = {}
    for i in range(100):
        k, v = random.randint(0, 100), random.randint(0, 100)
        generated[k] = v
        rbt.add(k, v)
        check_invariants(rbt._tree)
    for k, v in generated.items():
        assert rbt.get(k) == v
