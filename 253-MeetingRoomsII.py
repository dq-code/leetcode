# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        booked = []
        intervals = sorted(intervals, key=lambda interval:interval.start)
        for cur in intervals:
            need_new_room = True
            for i, past in enumerate(booked):
                if cur.start>=past.end:
                    booked[i] = cur
                    need_new_room = False
                    break
            if need_new_room:
                booked.append(cur)
        return len(booked)