class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1

        for i in range(length):
            if abs(nums[i]) <= length:
                curr = abs(nums[i]) - 1
                nums[curr] = -abs(nums[curr])

        for i in range(length):
            if nums[i] > 0:
                return i + 1

        return length + 1
