# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        intervals = sorted(intervals, key=lambda interval: (interval.start, interval.end))
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                if intervals[i].end > res[-1].end:
                    res[-1].end = intervals[i].end
            else:
                res.append(intervals[i])

        return res