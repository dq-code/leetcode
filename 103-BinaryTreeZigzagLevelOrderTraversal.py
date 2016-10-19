# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        res = []
        stack = [[root, 1, True]]
        while len(stack) > 0:
            data = stack.pop(0)
            node = data[0]
            # print "pop %d"%node.val
            level = data[1]
            rightFirst = data[2]

            if len(res) < level:
                res.append([node.val])
            else:
                if level % 2 == 1:
                    res[level - 1].insert(0, node.val)
                else:
                    res[level - 1].append(node.val)

            if node.right:
                # print "push %d"%node.right.val
                stack.append([node.right, level + 1, False])
            if node.left:
                # print "push %d"%node.left.val
                stack.append([node.left, level + 1, False])

        return res
