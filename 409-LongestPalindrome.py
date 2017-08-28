import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        counter = collections.Counter(s)
        res = 0
        odd = 0
        for v in counter.itervalues():
            res += v
            if v % 2 == 1:
                res -= 1
                odd += 1

        if odd > 0: res += 1

        return res
