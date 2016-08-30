# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSearch(self, node):
        if node == None: return
        self.inorderSearch(node.left)

        if self.prev != None and self.prev.val > node.val:
            self.n2 = node
            if self.n1 == None: self.n1 = self.prev

        self.prev = node

        self.inorderSearch(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.n1 = self.n2 = self.prev = None
        self.inorderSearch(root)
        temp = self.n1.val
        self.n1.val = self.n2.val
        self.n2.val = temp
