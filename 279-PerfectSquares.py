class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [n for i in range(n + 1)]
        j = 1
        while True:
            if j * j > n: break
            dp[j * j] = 1
            j += 1
        for i in range(1, n):
            j = 1
            while j * j + i <= n:
                dp[j * j + i] = min(dp[j * j + i], dp[i] + 1)
                j += 1
        return dp[-1]

