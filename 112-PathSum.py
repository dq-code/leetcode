# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, sum):
        subsum = sum - node.val
        left = False
        if node.left != None:
            left = self.helper(node.left, subsum)
        right = False
        if node.right != None:
            right = self.helper(node.right, subsum)
        if node.left == None and node.right == None:
            # print "no left and right nodes"
            return subsum == 0
        return left or right

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        return self.helper(root, sum)
