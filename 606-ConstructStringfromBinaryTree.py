# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def preorder(node):
            if not node: return ''
            res = str(node.val)
            if not node.right and node.left:
                res += '(' + preorder(node.left) + ')'
            elif node.right:
                res += '(' + preorder(node.left) + ')' + '(' + preorder(node.right) + ')'
            return res

        return preorder(t)

    