import collections


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 0, cooldown; -1, buy; 1 sell
        # dp = collections.defaultdict(set)
        # dp[0].add(0)
        #
        # for i in range(len(prices)):
        #     ndp = collections.defaultdict(set)
        #     for profit in dp.keys():
        #         for op in dp[profit]:
        #             if op == 0:
        #                 ndp[profit - prices[i]].add(-1)
        #             if op == -1:
        #                 ndp[profit + prices[i]].add(1)
        #             if op == 1:
        #                 ndp[profit].add(0)
        #
        #     dp = ndp
        # return max(dp.keys())

        if len(prices) < 2: return 0
        sells = [0 for i in range(len(prices))]
        buys = [0 for i in range(len(prices))]

        buys[0] = -prices[0]
        buys[1] = max(-prices[0], -prices[1])
        sells[1] = max(0, prices[1] - prices[0])

        for i in range(2, len(prices)):
            sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])
            buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])
        return sells[-1]

