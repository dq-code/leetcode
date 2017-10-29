from collections import Counter
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d, key=lambda w:len(w), reverse=True)
        res = ''
        for w in d:
            if (-len(w), w) < (-len(res), res):
                it = iter(s)
                if all(c in it for c in w):
                    res = w
        return res