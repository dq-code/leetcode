# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x.start)

        interval_stack = []
        interval_stack.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i].start > interval_stack[-1].end:
                interval_stack.append(intervals[i])
            elif intervals[i].end > interval_stack[-1].end:
                temp = interval_stack.pop()
                new_interval = Interval(temp.start, intervals[i].end)
                interval_stack.append(new_interval)

        return interval_stack
