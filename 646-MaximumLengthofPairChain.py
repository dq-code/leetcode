import sys
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, lambda x:x[1])
        res = 0
        end = -(sys.maxint-1)
        for pair in pairs:
            if pair[0]>end:
                res += 1
                end = pair[1]

        return res