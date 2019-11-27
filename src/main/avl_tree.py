
class TreeNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.parent = None
        self.balance_factor = 0


class AvlTree:

    def __init__(self, k, v):
        self._tree = TreeNode(k, v)

    def add(self, k, v):
        node = self._add(k, v)
        if node:
            self._rebalance(node)

    def _add(self, k, v):
        node = self._tree
        while node:
            if k < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(k, v)
                    node.left.parent = node
                    return node.left
            elif node.key < k:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(k, v)
                    node.right.parent = node
                    return node.right
            else:
                node.value = v
                return

    def _rebalance(self, node):
        pass

    def remove(self, k, v):
        pass

    def get(self, v):
        pass

    def _rotate_left(self, node):
        pass

    def _rotate_right(self, node):
        pass