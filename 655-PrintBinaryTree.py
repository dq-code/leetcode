# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def getDepth(node):
            if not node: return 0
            return max(getDepth(node.left), getDepth(node.right))+1

        if not root: return []
        depth = getDepth(root)
        width = 2**depth-1
        res = [["" for i in range(width)] for j in range(depth)]

        def helper(node, row, col, width):
            if not node: return

            res[row][col] = str(node.val)
            next_width = (width-1)/2
            helper(node.left, row+1, col-next_width-1, next_width)
            helper(node.right, row+1, col+next_width+1, next_width)

        next_width = (width-1)/2
        helper(root, 0, next_width, next_width)
        return res
