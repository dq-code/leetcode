class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for value in coins:
                if dp[i]>=0 and value+i <= amount:
                    dp[value+i] = min(dp[i] + 1, dp[value+i]) if dp[value+i]>0 else dp[i] + 1
        #print dp
        return dp[amount]