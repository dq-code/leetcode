class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.stack = []
        self.list = [v1, v2]

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            element = self.stack.pop(0)
            index = element[0]
            if self.list[index]:
                self.stack.append((index, self.list[index].pop(0)))
            return element[1]
        return -1

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            for i, l in enumerate(self.list):
                if l:
                    self.stack.append((i, l.pop(0)))
        return self.stack



        # Your ZigzagIterator object will be instantiated and called as such:
        # i, v = ZigzagIterator(v1, v2), []
        # while i.hasNext(): v.append(i.next())