# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, n1, n2):
        if n1 == None and n2 == None: return True
        if n1 and n2 and n1.val == n2.val: return self.isSameTree(n1.left, n2.right) and self.isSameTree(n1.right,
                                                                                                         n2.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True

        return self.isSameTree(root.left, root.right)
