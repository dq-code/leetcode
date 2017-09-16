# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0

        def getDepth(node):
            if not node: return 0
            leftD = getDepth(node.left)
            rightD = getDepth(node.right)
            self.max_diameter = max(self.max_diameter, leftD + rightD)
            return max(leftD, rightD) + 1

        getDepth(root)
        return self.max_diameter
