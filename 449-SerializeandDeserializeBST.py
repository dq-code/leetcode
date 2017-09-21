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
        if not root: return ""
        stack = [root]
        res = ""
        while stack:
            childs = []
            for node in stack:
                if not node:
                    res += ","
                    childs.append(None)
                    childs.append(None)
                else:
                    res += str(node.val)+","
                    childs.append(node.left)
                    childs.append(node.right)
            if childs.count(None) == len(childs):
                stack = []
            else:
                stack = childs
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        data = data.split(",")[:-1]
        length = len(data)
        index = 1
        root = TreeNode(data[0])
        parents = [root]
        while index<length:
            childs = []
            for i,node in enumerate(parents):
                if not node:
                    childs.append(None)
                    childs.append(None)
                    continue
                l,r = index+2*i,index+2*i+1
                left,right= data[index+2*i], data[index+2*i+1]
                node.left = None if left=="" else TreeNode(int(left))
                node.right = None if right == "" else TreeNode(int(right))
                childs.append(node.left)
                childs.append(node.right)
            if childs.count(None) == len(childs):
                break
            parents = childs
            index = index+2*i+2


        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))