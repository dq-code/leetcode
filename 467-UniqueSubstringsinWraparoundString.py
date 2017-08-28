import collections
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        pattern = 'abcdefghijklmnopqrstuvwxyza'
        cmap = collections.defaultdict(int)
        dp = [1 for i in range(len(p))]
        for i in range(len(p)):
            if i and p[i-1:i+1] in pattern:
                dp[i] += dp[i-1]
            cmap[p[i]] = max(cmap[p[i]], dp[i])


        return sum(cmap.values())


