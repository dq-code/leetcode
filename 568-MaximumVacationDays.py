class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        weeks = len(days[0])
        citys = len(days)
        dp = [-1 for j in range(citys)]
        dp[0] = 0

        for i in range(weeks):
            ndp = [-1 for j in range(citys)]
            for j in range(citys):
                if dp[j] < 0:
                    continue
                for k in range(citys):
                    if k == j or flights[j][k] > 0:
                        ndp[k] = max(ndp[k], dp[j] + days[k][i])
            dp = ndp
        return max(dp)
