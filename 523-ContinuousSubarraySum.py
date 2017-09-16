class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dp = {0:-1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            mod = total%k if k else total
            if mod not in dp:
                dp[mod] = i
            elif dp[mod]<=i-2:
                return True
        return False