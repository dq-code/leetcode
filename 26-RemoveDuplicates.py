class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if unique < i:
                    nums[unique] = nums[i]
                unique += 1
        return unique
