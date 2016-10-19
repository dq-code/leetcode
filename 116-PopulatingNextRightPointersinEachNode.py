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
        if root == None: return
        queue = [[root, 0]]
        temp_queue = []
        while len(queue) > 0:
            pair = queue.pop(0)
            node = pair[0]
            level = pair[1]

            if node.left != None:
                queue.append([node.left, level + 1])
            if node.right != None:
                queue.append([node.right, level + 1])

            temp_queue.append(node)
            if len(queue) == 0 or queue[0][1] > level:
                next = None
                cur = temp_queue.pop(0)
                while len(temp_queue) > 0:
                    next = temp_queue.pop(0)
                    cur.next = next
                    cur = next
                cur.next = None
        return
