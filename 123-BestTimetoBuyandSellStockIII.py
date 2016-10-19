class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0

        prevProfit = [0 for x in range(len(prices))]
        afterProfit = [0 for x in range(len(prices))]

        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            prevProfit[i] = max(prevProfit[i - 1], prices[i] - minPrice)

        maxPrice = prices[len(prices) - 1]
        for i in range(len(prices) - 2, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            afterProfit[i] = max(afterProfit[i + 1], maxPrice - prices[i])

        maxProfit = 0
        for i in range(0, len(prices)):
            maxProfit = max(maxProfit, prevProfit[i] + afterProfit[i])

        return maxProfit
