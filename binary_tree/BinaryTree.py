# from queue.Queue import Queue
from queue_own.Queue import Queue
from stack.Stack import Stack


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        """root -> left -> right"""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.postorder_print(start.right, traversal)
        return traversal

    def level_order(self, root, traversal):
        if root is None:
            return

        queue = Queue()
        queue.enqueue(root)

        while len(queue) > 0:
            traversal.append(queue.peek().value)
            node = queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        return traversal

    def reverse_level_order(self, root):
        if root is None:
            return
        stack = Stack()
        queue = Queue()
        queue.enqueue(root)
        traversal = []

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right is not None:
                queue.enqueue(node.right)
            if node.left is not None:
                queue.enqueue(node.left)

        while len(stack) > 0:
            traversal.append(stack.pop().value)
        return traversal

    def height(self, root):
        if root is None:
            return -1
        left_tree = self.height(root.left)
        right_tree = self.height(root.right)
        return 1 + max(left_tree, right_tree)

    def size(self):
        """How many node in the binary tree"""
        stack = Stack()
        stack.push(self.root)
        count = 1
        while stack:
            node = stack.pop()
            if node.left:
                count += 1
                stack.push(node.left)
            if node.right:
                count += 1
                stack.push(node.right)
        return count

    def size_(self, root):
        """the left subtree of root node + right subtree of root node"""
        if root is None:
            return 0
        return 1 + self.size_(root.left) + self.size_(root.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

"""
                      height
            1           2
          /   \         
        2       3       1
       / \     /  \     
      4   5   6    7    0

"""
print(tree.size())
