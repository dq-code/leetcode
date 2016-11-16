# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        res = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack[0]
            if node.left == None and node.right == None:
                res.append(node.val)
                stack.pop(0)
            else:
                if node.right:
                    stack.insert(0, node.right)
                    node.right = None
                if node.left:
                    stack.insert(0, node.left)
                    node.left = None

        return res
