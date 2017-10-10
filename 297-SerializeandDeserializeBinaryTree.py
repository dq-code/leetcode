# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                res.append("#")
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        # print res
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper():
            # print self.index
            if self.index >= len(dataLS): return None
            if dataLS[self.index] == '#':
                self.index += 1
                return None
            root = TreeNode(int(dataLS[self.index]))
            self.index += 1
            root.left = helper()
            root.right = helper()
            return root

        self.index = 0
        dataLS = data.split()
        # print dataLS
        return helper()


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))