# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        total = 0
        if root.left and not root.left.right and not root.left.left:
            total+= root.left.val
        total+= self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return total