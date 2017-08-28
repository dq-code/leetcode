import collections


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.Counter()
        dp[0] = 1
        for i in range(len(nums)):
            ndp = collections.Counter()
            for k in dp.keys():
                ndp[k + nums[i]] += dp[k]
                ndp[k - nums[i]] += dp[k]
            dp = ndp
        return dp[S]
