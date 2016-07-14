class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[length-1]:
                nums[i],nums[length] = nums[length],nums[i]
                length = length + 1

        return length
