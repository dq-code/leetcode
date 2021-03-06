class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = max(maxSum, curSum)

        return maxSum
