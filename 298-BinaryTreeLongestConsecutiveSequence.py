# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.max_len = 0
        def helper(node, length):
            if node.left and node.val+1==node.left.val:
                helper(node.left,length+1)
            else:
                self.max_len = max(self.max_len,length)
                if node.left:
                    helper(node.left, 1)
            if node.right and node.val+1 == node.right.val:
                helper(node.right, length+1)
            else:
                self.max_len = max(self.max_len,length)
                if node.right:
                    helper(node.right, 1)
        helper(root, 1)
        return self.max_len