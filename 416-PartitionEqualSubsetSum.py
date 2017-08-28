class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        total = sum(nums)
        if total % 2 != 0: return False
        subTotal = total / 2
        dp = [0 for i in range(subTotal + 1)]
        dp[0] = 1

        for j in nums:
            # print j
            ndp = list(dp)
            for i in range(subTotal + 1):
                if i + j <= subTotal and dp[i] == 1: ndp[i + j] = 1
            dp = list(ndp)
            # print dp
        return dp[-1] == 1
