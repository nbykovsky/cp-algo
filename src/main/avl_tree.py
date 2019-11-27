
class TreeNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.balance_factor = 0


class AvlTree:

    def __init__(self, k, v):
        self._tree = TreeNode(k, v)

    def add(self, k, v):
        pass

    def remove(self, k, v):
        pass

    def get(self, v):
        pass

    def _rotate_left(self, node):
        pass

    def _rotate_right(self, node):
        pass