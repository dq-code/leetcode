class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        dp = [1 for i in range(len(nums))]
        prev = [-1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1 > dp[i]:
                    dp[i] = max(dp[j]+1, dp[i])
                    prev[i] = j
        index = dp.index(max(dp))
        res= [index]
        while index >= 0:
            pre = prev[index]
            res.append(pre)
            index = pre
        return res
