# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            children = []
            for node, i in queue:
                cols[i].append(node.val)
                if node.left:
                    children.append((node.left, i - 1))
                if node.right:
                    children.append((node.right, i + 1))
            queue = children

        return [cols[key] for key in sorted(cols)]
