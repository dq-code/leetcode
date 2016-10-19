class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0

        if len(prices) <= 1: return res

        localMin = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < localMin: localMin = prices[i]
            res = max(res, prices[i] - localMin)

        return res
