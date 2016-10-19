# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0:
            mininum = right
        elif right == 0:
            mininum = left
        else:
            mininum = min(right, left)

        return mininum + 1
