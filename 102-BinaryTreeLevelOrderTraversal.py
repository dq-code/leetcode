# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        stack = [[root, 1]]
        res = []
        while len(stack) > 0:
            pair = stack.pop()
            level = pair[1]
            node = pair[0]
            if len(res) < level:
                res.append([node.val])
            else:
                res[level - 1].append(node.val)

            if node.right:
                stack.append([node.right, level + 1])
            if node.left:
                stack.append([node.left, level + 1])

        return res
