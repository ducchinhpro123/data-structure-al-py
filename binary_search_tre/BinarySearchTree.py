class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def insert_iterative(self, new_value):
        # if the tree is empty: initialize root of the tree
        if self.root is None:
            self.root = Node(new_value)
            return

        cur, prev = self.root, None
        while cur is not None:
            if cur.data == new_value:
                return
            prev = cur
            if cur.data < new_value:
                cur = cur.right
            else:
                cur = cur.left
        node = Node(new_value)
        if prev.data < new_value:
            prev.right = node
        else:
            prev.left = node

    def search(self, find_val) -> Node | None:
        cur = self.root
        while cur is not None:
            if cur.data < find_val:
                cur = cur.right
            elif cur.data > find_val:
                cur = cur.left
            else:
                break
        return cur

    def search_recursive(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)

    def is_bst_satisfied(self):
        def helper(root, min_val=float('-inf'), max_val=float('inf')):
            if not root:
                return True

            val = root.data
            if val <= min_val or val >= max_val:
                return False
            if not helper(root.right, val, max_val):
                return False
            if not helper(root.left, min_val, val):
                return False
            return True

        return helper(self.root)

    """
    AVL trees are both binary search trees and balanced binary search trees, 
    satisfying all the properties of both types of binary trees, 
    so they are also called "balanced binary search trees".
    """


bst = BST(8)
bst.insert(12)
bst.insert(2)
bst.insert(6)
bst.insert(10)
bst.insert(14)
print(bst.is_bst_satisfied())
