"""
Invariants
1. All nodes must be "colored" either red or black
2. The root of the tree must be black
3. If a node is red, all of its children must be black
    (i.e., we can’t have a red node with a red child)
4. For any given node u, every possible path from u to a "null reference"
    (i.e., an empty left or right child) must contain the same number of black nodes

"""

from typing import Optional


class Node:
    BLACK = "black"
    RED = "red"

    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self._tree: Optional[Node] = None

    def add(self, key, value):
        if not self._tree:
            self._tree = Node(key, value, Node.BLACK)
        else:
            self._add(key, value, self._tree)
            if self._tree.color == Node.RED:
                self._tree.color = Node.BLACK

    def remove(self, key):
        raise NotImplementedError()

    def get(self, key):
        return self._get(key, self._tree)

    def get_at(self, pos):
        raise NotImplementedError()

    def _add(self, key, value, tree):
        if not tree:
            raise ValueError("Tree shouldn't be empty")

        if (
            tree.color == Node.BLACK
            and tree.left
            and tree.left.color == Node.RED
            and tree.right
            and tree.right.color == Node.RED
        ):
            tree.color = Node.RED
            tree.right.color = tree.left.color = Node.BLACK
            if tree.parent and tree.parent.color == Node.RED:
                self._fix_color(tree.parent)

        if key > tree.key:
            if tree.right:
                self._add(key, value, tree.right)
            else:
                tree.right = Node(key, value, Node.RED)
                tree.right.parent = tree
                if tree.color == Node.RED:
                    self._fix_color(tree)
        elif key < tree.key:
            if tree.left:
                self._add(key, value, tree.left)
            else:
                tree.left = Node(key, value, Node.RED)
                tree.left.parent = tree
                if tree.color == Node.RED:
                    self._fix_color(tree)
        else:
            tree.value = value

    def _fix_color(self, top_red_node):
        if not top_red_node.parent:
            top_red_node.color = Node.BLACK
        elif self._is_left(top_red_node):
            if top_red_node.right and top_red_node.right.color == Node.RED:
                self._rotate_left(top_red_node)
                top_red_node = top_red_node.parent
            self._rotate_right(top_red_node.parent)
            top_red_node.right.color = Node.RED
        else:
            if top_red_node.left and top_red_node.left.color == Node.RED:
                self._rotate_right(top_red_node)
                top_red_node = top_red_node.parent
            self._rotate_left(top_red_node.parent)
            top_red_node.left.color = Node.RED
        top_red_node.color = Node.BLACK

    def _rotate_right(self, node):
        if not node.parent:
            self._tree = node.left
            node.left.parent = None
        elif self._is_left(node):
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent
        bk = node.left.right
        node.left.right = node
        node.parent = node.left
        node.left = bk
        if bk:
            bk.parent = node

    @staticmethod
    def _is_left(node):
        return node.parent.left and node.parent.left == node

    def _rotate_left(self, node):
        if not node.parent:
            self._tree = node.right
            node.right.parent = None
        elif self._is_left(node):
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent
        bk = node.right.left
        node.right.left = node
        node.parent = node.right
        node.right = bk
        if bk:
            bk.parent = node

    def _get(self, key, tree: Node):
        if not tree:
            raise IndexError(f"Key {key} does not exists")

        if key > tree.key:
            return self._get(key, tree.right)
        elif key < tree.key:
            return self._get(key, tree.left)
        else:
            return tree.value
