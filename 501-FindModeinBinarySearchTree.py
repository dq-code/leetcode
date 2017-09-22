# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        modes = collections.Counter()

        def helper(node):
            if not node: return
            modes[node.val] += 1
            helper(node.left)
            helper(node.right)

        helper(root)
        max_count = max(modes.values() + [None])
        return [k for k, v in modes.iteritems() if v == max_count]

