# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None

        pre, cur = None, root
        while cur and cur.val!=key:
            pre = cur
            if cur.val > key:
                cur = cur.left
            elif cur.val < key:
                cur = cur.right
        if not cur: return root

        def maxChild(node):
            while node.right:
                node = node.right
            return node

        ncur = cur.right
        if cur.left:
            ncur = cur.left
            maxChild(cur.left).right = cur.right
        if not pre: return ncur

        if pre.left == cur:
            pre.left = ncur
        else:
            pre.right = ncur

        return root

