import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for x1, y1 in points:
            dist_map = collections.defaultdict(int)
            for x2, y2 in points:
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dist_map[dist] += 1
            for v in dist_map.itervalues():
                res += v * (v - 1)

        return res