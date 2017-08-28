import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        edge_map = collections.defaultdict(int)
        for i in range(len(wall)):
            edge = 0
            for j in range(len(wall[i]) - 1):
                edge += wall[i][j]
                edge_map[edge] += 1

        if len(edge_map) == 0: return len(wall)
        return len(wall) - collections.Counter(edge_map).most_common()[0][1]




