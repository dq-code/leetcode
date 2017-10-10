# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def findLevel(node, level):
            if not node: return level
            return findLevel(node.right,level+1)
        level = findLevel(root, 0)
        curLevel = 0
        stack = [root]
        while curLevel<level:
            curLevel += 1
            children = []
            for node in stack:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            stack = children
        return 2**(level)-1+len(children)