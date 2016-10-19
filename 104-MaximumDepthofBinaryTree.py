# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, depth):
        if node == None:
            if depth > self.max: self.max = depth
            return

        self.helper(node.right, depth + 1)
        self.helper(node.left, depth + 1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.helper(root, 0)
        return self.max
