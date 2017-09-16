# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def helper(node, val):
            if not node: return 0
            res = 1 if node.val == val else 0
            res += helper(node.left, val - node.val)
            res += helper(node.right, val - node.val)
            return res

        if not root: return 0

        res = helper(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res