class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[y] = nums[y], nums[i]
                y += 1
