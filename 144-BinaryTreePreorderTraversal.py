# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        res = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.val)
            if node.right: queue.insert(0, node.right)
            if node.left: queue.insert(0, node.left)

        return res
