class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            tempMax = curMax * nums[i]
            tempMin = curMin * nums[i]
            curMax = max(max(tempMax, tempMin), nums[i])
            curMin = min(min(tempMax, tempMin), nums[i])

            result = max(result, curMax)

        return result
