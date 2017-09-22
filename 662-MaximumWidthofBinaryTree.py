# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack = [[root,0]]
        max_width = 0
        while stack:
            children = []
            for pair in stack:
                if pair[0].left: children.append([pair[0].left, pair[1]*2])
                if pair[0].right: children.append([pair[0].right, pair[1] * 2+1])
            max_width = max(max_width, stack[-1][1]-stack[0][1]+1)

            stack = children
        return max_width
