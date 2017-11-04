import collections


class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = collections.deque()
        self.num = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1
        self.num += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.hits and (timestamp - self.hits[0][0]) >= 300:
            self.num -= self.hits.popleft()[1]
        return self.num




        # Your HitCounter object will be instantiated and called as such:
        # obj = HitCounter()
        # obj.hit(timestamp)
        # param_2 = obj.getHits(timestamp)