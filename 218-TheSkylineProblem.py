from heapq import *


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings: return []
        liveBld = []
        res = []
        cur = 0
        num = len(buildings)
        while cur < num or liveBld:
            curX = buildings[cur][0] if not liveBld else -liveBld[0][1]
            if cur >= num or buildings[cur][0] > curX:
                while liveBld and -liveBld[0][1] <= curX:
                    heappop(liveBld)
            else:
                curX = buildings[cur][0]
                while cur < num and buildings[cur][0] == curX:
                    heappush(liveBld, [-buildings[cur][2], -buildings[cur][1]])
                    cur += 1

            curY = 0 if not liveBld else -liveBld[0][0]
            if not res or res[-1][1] != curY: res.append((curX, curY))

        return res