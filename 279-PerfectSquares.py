class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(1, n+1):
            j = 1
            while True:
                square = j*j
                if i+square > n: break
                if dp[i+square] > 0:
                    dp[i+square] = min(dp[i+square], dp[square]+dp[i])
                else:
                    dp[i + square] = dp[square]+dp[i]
                j = j + 1
        return dp[-1]

