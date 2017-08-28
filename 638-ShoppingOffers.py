class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        dp = {}

        def helper(needs):
            if needs in dp: return dp[needs]
            dp[needs] = sum(x*y for x,y in zip(price, needs))
            for deal in special:
                rest = tuple(x-y for x,y in zip(needs,deal))
                if min(rest) < 0: continue
                dp[needs] = min(dp[needs], deal[-1]+helper(rest))
            return dp[needs]

        return helper(tuple(needs))
