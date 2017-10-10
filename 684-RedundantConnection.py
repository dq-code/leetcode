class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.parent = None

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        res = []
        map = {}

        for edge in edges:
            if edge[0] not in map:
                parent = TreeNode(edge[0])
                child = TreeNode(edge[1])
                child.parent = parent
                parent.left = child
                map[edge[0]] = parent
                map[edge[1]] = child
            else:
                if edge[1] not in map:
                    child = TreeNode(edge[1])
                    map[edge[1]] = child
                child = map[edge[1]]
                parent = map[edge[0]]

                if child.parent!=None:
                    res.append(edge)
                else:
                    if parent.left and parent.right:
                        res.append(edge)
                        continue
                    child.parent = parent
                    if not parent.left:
                        parent.left = child
                    elif not parent.right:
                        parent.right = child


        return res[-1] if len(res)>0 else []

