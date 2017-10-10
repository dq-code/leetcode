# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = [root]
        res = []
        while stack:
            children = []
            cur_list = []
            for node in stack:
                cur_list.append(node.val)
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            res.append(cur_list)
            stack = children
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = list(reversed(res[i]))
        return res
