# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0
        def helper(node):
            if not node: return
            helper(node.right)
            node.val += self.total
            self.total = node.val
            helper(node.left)
        helper(root)
        return root