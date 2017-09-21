# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return [0,0]
            robleft = dfs(node.left)
            robright = dfs(node.right)
            norobRoot = max(robleft[1], robleft[0]) + max(robright[0], robright[1])
            robRoot = node.val + robleft[0] + robright[0]
            return [norobRoot, robRoot]

        return max(dfs(root))


