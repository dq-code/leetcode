# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        stack = [root]
        res = []
        while stack:
            res.append(stack[0].val)
            children = []
            for node in stack:
                if node.right: children.append(node.right)
                if node.left: children.append(node.left)
            stack = children
        return res


