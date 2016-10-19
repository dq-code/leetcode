# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, sum, list):
        subsum = sum - node.val
        newList = list + [node.val]

        if node.left != None:
            self.helper(node.left, subsum, newList)
        if node.right != None:
            self.helper(node.right, subsum, newList)
        if node.left == None and node.right == None:
            if subsum == 0:
                self.res.append(newList)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None: return []
        self.res = []
        self.helper(root, sum, [])
        return self.res
