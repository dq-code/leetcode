# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node, val):
            if not node:
                return True
            r, l = helper(node.right, node.val), helper(node.left, node.val)
            if not r or not l: return False
            self.count += 1
            return node.val == val

        self.count = 0
        helper(root, 0)
        return self.count
