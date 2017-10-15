# Definition for an interval.
from operator import attrgetter
#class Interval(object):
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals = sorted(intervals, key=attrgetter('start','end'))
        #print intervals
        res = []
        for tt in intervals:
            if not res: res.append(tt)
            else:
                prev = res[-1]
                if prev.end < tt.start:
                    res.append(tt)
                else:
                    prev.end = max(prev.end, tt.end)
        return res