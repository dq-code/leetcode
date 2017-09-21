# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack = [root]
        res = []
        while stack or childs:
            values = []
            childs = []
            for node in stack:
                values.append(node.val)
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            res.append(max(values))
            stack = childs
        return res