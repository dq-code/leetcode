# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = collections.defaultdict(list)
        def helper(node):
            if not node:
                return "#"
            flat_tree = "%s(%s,%s)"%(node.val, helper(node.left), helper(node.right))
            res[flat_tree].append(node)
            return flat_tree
        helper(root)
        return [v[0] for v in res.values() if len(v)>1]