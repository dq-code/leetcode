# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        list = []
        def helper(node):
            if not node: return
            helper(node.left)
            list.append(node.val)
            helper(node.right)

        helper(root)
        start = 0
        end = len(list)-1
        while start<end:
            cur = list[start]+list[end]
            if cur==k:
                return True
            if cur<k:
                start+=1
            else:
                end -= 1
        return False
