# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def helper(node1, node2):
            if not node1 and not node2: return True
            if node1 and node2 and node1.val == node2.val:
                return helper(node1.left, node2.left) and helper(node1.right, node2.right)
            return False

        if not t: return True
        if not s: return False

        if s.val == t.val and helper(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)