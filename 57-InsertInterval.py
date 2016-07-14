# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def helper(self, needToBeIntersertedInterval):
        if self.interval_stack[-1].end < needToBeIntersertedInterval.start:
            self.interval_stack.append(needToBeIntersertedInterval)
        elif self.interval_stack[-1].end < needToBeIntersertedInterval.end:
            temp = self.interval_stack.pop()
            new_interval = Interval(temp.start, needToBeIntersertedInterval.end)
            self.interval_stack.append(new_interval)

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]

        self.interval_stack = []
        inserted = False
        for i in range(len(intervals)):
            if not inserted and newInterval.start < intervals[i].start:
                if len(self.interval_stack) == 0:
                    self.interval_stack.append(newInterval)
                else:
                    self.helper(newInterval)
                inserted = True
            elif len(self.interval_stack) == 0:
                self.interval_stack.append(intervals[i])
            self.helper(intervals[i])

        if not inserted:
            self.helper(newInterval)

        return self.interval_stack
