# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0: return None

        root = TreeNode(postorder[-1])
        inorder_index = inorder.index(postorder[-1])
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder[inorder_index:-1])
        root.left = self.helper(inorder[:inorder_index],postorder[:inorder_index])

        return root

