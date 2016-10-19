# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None: return 0
        lenStartFromLeft = self.helper(root.left)
        lenStartFromRight = self.helper(root.right)
        sum = root.val
        if self.maxSum < sum: self.maxSum = sum
        if lenStartFromLeft > 0:
            sum += lenStartFromLeft
            if self.maxSum < sum: self.maxSum = sum
        if lenStartFromRight > 0:
            sum += lenStartFromRight
            if self.maxSum < sum: self.maxSum = sum

        res = max(root.val, root.val + lenStartFromLeft, root.val + lenStartFromRight)
        return res

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = -10000000
        self.helper(root)

        return self.maxSum
