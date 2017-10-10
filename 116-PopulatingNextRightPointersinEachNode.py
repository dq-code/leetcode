# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return
        stack = [root]
        while stack:
            children = []
            length = len(stack)
            for index, node in enumerate(stack):
                if index+1<length:
                    node.next = stack[index+1]
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            stack = children
        return