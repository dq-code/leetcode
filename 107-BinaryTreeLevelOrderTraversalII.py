# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        queue = [[root, 1]]
        res = []
        while len(queue) > 0:
            pair = queue.pop(0)
            node = pair[0]
            level = pair[1]
            # print "node is %d and level is %d"%(node.val, level)
            # print res
            if len(res) < level:
                res.insert(0, [node.val])
            else:
                res[0].append(node.val)

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
        return res
