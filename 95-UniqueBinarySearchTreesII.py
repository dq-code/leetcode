# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, start, end):
        if start > end: return [None]

        res = []
        for i in range(start, end + 1):
            leftTree = self.helper(start, i - 1)
            rightTree = self.helper(i + 1, end)
            for l in leftTree:
                for r in rightTree:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0: return []
        res = self.helper(1, n)

        return res
