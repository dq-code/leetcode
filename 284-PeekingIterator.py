# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nval = None
        self.iter = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.nval:
            if self.hasNext():
                return self.nval
            else:
                return None
        else:
            return self.nval

    def next(self):
        """
        :rtype: int
        """
        if self.nval:
            temp = self.nval
            self.nval = None
            return temp
        else:
            temp = self.peek()
            self.nval = None
            return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nval: return True
        if self.iter.hasNext():
            self.nval = self.iter.next()
            return True
        self.nval = None
        return False



        # Your PeekingIterator object will be instantiated and called as such:
        # iter = PeekingIterator(Iterator(nums))
        # while iter.hasNext():
        #     val = iter.peek()   # Get the next element but not advance the iterator.
        #     iter.next()         # Should return the same value as [val].