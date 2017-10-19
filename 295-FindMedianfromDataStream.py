from heapq import *


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.leftheap = []
        self.rightheap = []
        self.left_size = 0
        self.right_size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.rightheap:
            heappush(self.leftheap, -num)
            self.left_size += 1
        else:
            if num >= self.rightheap[0]:
                heappush(self.rightheap, num)
                self.right_size += 1
            else:
                heappush(self.leftheap, -num)
                self.left_size += 1

        while self.left_size - self.right_size > 1:
            heappush(self.rightheap, -heappop(self.leftheap))
            self.left_size -= 1
            self.right_size += 1

        while self.right_size > self.left_size:
            heappush(self.leftheap, -heappop(self.rightheap))
            self.left_size += 1
            self.right_size -= 1

            # print "left"
            # print self.leftheap
            # print "right"
            # print self.rightheap

    def findMedian(self):
        """
        :rtype: float
        """
        if self.right_size == self.left_size:
            # print self.leftheap[0]
            # print self.rightheap[0]
            return float(-self.leftheap[0] + self.rightheap[0]) / 2
        # print self.leftheap[0]
        return -float(self.leftheap[0])


        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()