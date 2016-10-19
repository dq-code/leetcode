class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0

        res = 0
        localMin = prices[0]

        for i in range(1, len(prices) - 1):
            if prices[i] >= prices[i - 1] and prices[i] >= prices[i + 1]:
                res += prices[i] - localMin
                localMin = prices[i + 1]

            if prices[i] < localMin:
                localMin = prices[i]

        if prices[len(prices) - 1] >= prices[len(prices) - 2]:
            res += prices[len(prices) - 1] - localMin

        return res
