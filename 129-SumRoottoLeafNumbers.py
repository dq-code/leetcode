# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, curSum):
        if node == None:
            return
        curSum = curSum * 10 + node.val
        if node.left:
            self.helper(node.left, curSum)
        if node.right:
            self.helper(node.right, curSum)
        if node.left == None and node.right == None:
            self.sum += curSum
            return

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.helper(root, 0)

        return self.sum
