# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return None
        map = {}
        queue = []
        clonedStarter = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = clonedStarter
        while len(queue) > 0:
            curNode = queue.pop()
            for neighbour in curNode.neighbors:
                if neighbour not in map:
                    newNode = UndirectedGraphNode(neighbour.label)
                    map[neighbour] = newNode
                    queue.append(neighbour)
                    map[curNode].neighbors.append(newNode)
                else:
                    map[curNode].neighbors.append(map[neighbour])

        return clonedStarter
