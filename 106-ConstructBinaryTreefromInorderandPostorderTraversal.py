# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, index, list):
        if len(list) == 0: return None
        if index < 0: return None

        root = TreeNode(self.postorder[index])
        i = list.index(root.val)

        root.left = self.helper(i-1, list[:i])
        root.right = self.helper(index-1, list[i+1:])
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        self.postorder = postorder

        return self.helper(len(self.postorder)-1, inorder)

