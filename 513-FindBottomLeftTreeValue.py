# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]
        i = 0
        childs = []
        while i<len(stack):
            if stack[i].left:
                childs.append(stack[i].left)
            if stack[i].right:
                childs.append(stack[i].right)
            i += 1
            if i==len(stack):
                if not childs:
                    break
                else:
                    i = 0
                    stack = childs
                    childs = []
        return stack[0].val
