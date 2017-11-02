# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node, val):
            if not node: return 0
            r, l = helper(node.right, node.val), helper(node.left, node.val)
            self.longest = max(self.longest, r + l + 1)
            return max(r + 1, l + 1) if node.val == val else 0

        self.longest = 0
        helper(root, 0)
        return self.longest - 1 if self.longest > 0 else 0
