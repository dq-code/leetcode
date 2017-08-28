# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
import collections
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)<3: return len(points)
        max_points = 0
        for i in range(len(points)):
            slope_map = collections.defaultdict(int)
            slope_map['INF'] = 0
            same_point = 1
            for j in range(len(points)):
                if i==j: continue
                if points[i].x==points[j].x and points[i].y!=points[j].y:
                    slope_map['INF'] += 1
                elif points[i].x!=points[j].x:
                    slope = 1.0*(points[i].y-points[j].y)/(points[i].x-points[j].x)
                    slope_map[slope]+=1
                else:
                    same_point+=1

            max_points = max(max_points, max(slope_map.values())+same_point)

        return max_points

