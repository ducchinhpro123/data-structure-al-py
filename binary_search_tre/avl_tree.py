class TreeNode:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def height(self, node):
        if node is not None:
            return node.height
        return -1

    def _update_height(self, root):
        h = max([self.height(root.left), self.height(root.right)]) + 1
        print(h)
        root.height = max([self.height(root.left), self.height(root.right)]) + 1

