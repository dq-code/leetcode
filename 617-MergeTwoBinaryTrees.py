# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: return t2
        if not t2: return t1

        def helper(node1, node2):
            if node1 and node2:
                node = TreeNode(node1.val + node2.val)
                node.left = helper(node1.left, node2.left)
                node.right = helper(node1.right, node2.right)
                return node
            elif node1 and not node2:
                node = TreeNode(node1.val)
                node.left = helper(node1.left, None)
                node.right = helper(node1.right, None)
                return node
            elif node2 and not node1:
                node = TreeNode(node2.val)
                node.left = helper(node2.left, None)
                node.right = helper(node2.right, None)
                return node

            return None

        return helper(t1, t2)