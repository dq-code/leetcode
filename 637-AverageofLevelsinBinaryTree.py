# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        stack = [root]
        res = []
        while stack:
            average = 1.0*(sum([n.val for n in stack]))/len(stack)
            res.append(average)
            childs = []
            for node in stack:
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            stack = childs

        return res