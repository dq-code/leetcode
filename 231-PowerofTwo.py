class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n: return False
        while n%2==0:
            n = n/2
        return n==1