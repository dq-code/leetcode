# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        tmp_left = self.invertTree(root.left)
        tmp_right = self.invertTree(root.right)
        root.left = tmp_right
        root.right = tmp_left
        return root
