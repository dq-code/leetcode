# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node):
        if node == None:
            return 1
        left = self.helper(node.left)
        if not left: return False

        right = self.helper(node.right)
        if not right: return False

        if abs(left - right) > 1: return False

        return max(left, right) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        res = self.helper(root)
        if not res: return res
        return True
