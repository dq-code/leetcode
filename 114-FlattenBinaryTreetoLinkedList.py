# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None: return None
        if root.left != None:
            print root.val
            temp = root.right
            # print "root left value is %d"%root.left.val
            node = self.helper(root.left)
            walker = node
            while walker.right != None:
                walker = walker.right
            walker.right = self.helper(temp)
            root.right = node
            root.left = None
        else:
            root.right = self.helper(root.right)
        # print "return root is %d"% root.val
        return root

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
