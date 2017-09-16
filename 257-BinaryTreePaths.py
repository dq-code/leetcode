# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def helper(node, path):
            if not node.left and not node.right: res.append(path)
            if node.left:
                helper(node.left, path+"->"+str(node.left.val))
            if node.right:
                helper(node.right, path+"->"+str(node.right.val))
        if not root: return []
        helper(root, str(root.val))
        return res