# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        index = 0
        while index < k:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                index+=1
                if index==k:
                    break
                node = node.right
        return node.val