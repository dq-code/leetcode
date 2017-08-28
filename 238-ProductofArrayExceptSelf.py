class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1 for i in range(len(nums))]
        left = 1
        for i in range(1, len(nums)):
            left *= nums[i - 1]
            output[i] = left
        right = 1
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            output[i] = output[i] * right

        return output