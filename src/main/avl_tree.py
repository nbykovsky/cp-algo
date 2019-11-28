
class TreeNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.parent = None
        self.balance_factor = 0
        self.height = 1        

class AvlTree:

    def __init__(self):
        self._tree = None

    def add(self, k, v):
        if not self._tree:
            self._tree = TreeNode(k, v)
            return
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

        get_height = lambda x: x.height if x else 0
        
        n = node
        while n:
            lh = get_height(n.left)
            rh = get_height(n.right)
            n.height = max(lh, rh) + 1
            balance_factor = lh - rh
            if balance_factor > 1:
                if get_height(n.left.left) < get_height(n.left.right):
                    self._rotate_left(n.left)
                self._rotate_right(n)
            elif balance_factor < -1:
                if get_height(n.right.right) < get_height(n.right.left):
                    self._rotate_right(n.right)
                self._rotate_left(n)
            else:
                n = n.parent
                

    def remove(self, k, v):
        pass

    def get(self, k):
        node = self._get_node(k)
        return node.value if node else -1
        
    def _get_node(self, k):
        if not self._tree:
            return None
        node = self._tree
        while node:
            if k < node.key:
                node = node.left
            elif node.key < k:
                node = node.right
            else:
                return node
        return None

    @staticmethod
    def _is_left(node):
        return node.parent.left == node

    def _rotate_right(self, node):
        if not node.parent:
            self._tree = node.left
            node.left.parent = None
        elif AvlTree._is_left(node):
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent
        bk = node.left.right
        node.left.right = node
        node.parent = node.left
        node.left = bk

    def _rotate_left(self, node):
        if not node.parent:
            self._tree = node.right
            node.right.parent = None
        elif AvlTree._is_left(node):
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent
        bk = node.right.left
        node.right.left = node
        node.parent = node.right
        node.right = bk

