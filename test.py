# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val==node2.val:
                return isSameTree(node1.left, node2.right) and isSameTree(node1.right, node2.left)
            return False

        if not root: return True
        return isSameTree(root.left, root.right)