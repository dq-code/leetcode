# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left: return -1
        self.secondMin = sys.maxint
        def helper(node):
            if not node: return
            if node.val > root.val:
                self.secondMin = min(self.secondMin,node.val)
            helper(node.right)
            helper(node.left)
        helper(root)
        return self.secondMin if self.secondMin<sys.maxint else -1