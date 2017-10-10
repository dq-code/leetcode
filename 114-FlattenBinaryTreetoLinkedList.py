# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return None

        def helper(prev, node):
            if not node: return None

            prev.right = node
            orig_right = node.right
            new_prev = node
            if node.left:
                next_node = node.left
                node.left = None
                new_prev = helper(node, next_node)
            if orig_right:
                new_prev = helper(new_prev, orig_right)
            return new_prev

        pivot = TreeNode(0)
        helper(pivot, root)
