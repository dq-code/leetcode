class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.stack = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.stack.append(val)
        while len(self.stack) > self.size:
            self.stack.pop(0)
        return float(sum(self.stack)) / len(self.stack)



        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param_1 = obj.next(val)