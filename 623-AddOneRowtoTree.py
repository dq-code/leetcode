# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            node = TreeNode(v)
            node.left = root
            return node

        curd = 1
        stack = [root]
        while curd < d-1:
            childs = []
            for node in stack:
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            stack = childs
            curd += 1

        for node in stack:
            old_left, old_right = node.left, node.right
            node.left, node.right = TreeNode(v), TreeNode(v)
            node.left.left, node.right.right = old_left, old_right

        return root
