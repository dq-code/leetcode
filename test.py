# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        stack = [root]
        res = []
        while stack:
            children = []
            vals = []
            for node in stack:
                vals.append(node.val)
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            stack=children
            res.append(vals)

        return res