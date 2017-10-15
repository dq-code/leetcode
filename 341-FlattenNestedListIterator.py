# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.iter = iter(nestedList)
        self.stack = []

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack: return True
        while True:
            nextNested = next(self.iter, None)
            if nextNested == None: return False

            if nextNested.isInteger():
                self.stack.append(nextNested.getInteger())
                return True

            nestedList = nextNested.getList()
            if nestedList:
                nestedList = self.flatList(nestedList)
                for e in nestedList[::-1]:
                    self.stack.append(e.getInteger())

            if self.stack: return True

        return False

    def flatList(self, nestedList):
        res = []
        for x in nestedList:
            if x.isInteger():
                res.append(x)
            else:
                nl = x.getList()
                if nl:
                    for y in self.flatList(x.getList()):
                        res.append(y)
        return res





        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())