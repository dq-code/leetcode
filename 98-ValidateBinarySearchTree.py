# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, min, max):
        if node.val >= max or node.val <= min: return False
        if node.left != None:
            if not self.helper(node.left, min, node.val): return False
        if node.right != None:
            if not self.helper(node.right, node.val, max): return False
        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True

        return self.helper(root, -2147483649, 2147483648)
