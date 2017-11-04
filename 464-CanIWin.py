class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        def helper(state, total):
            if state in dp: return dp[state]
            for i in range(maxChoosableInteger, 0, -1):
                if not state & (1 << (i - 1)):
                    if total + i >= desiredTotal or not helper(state | (1 << (i - 1)), total + i):
                        dp[state] = True
                        return True
            dp[state] = False
            return False

        if maxChoosableInteger >= desiredTotal: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal: return False
        dp = {}
        return helper(0, 0)
