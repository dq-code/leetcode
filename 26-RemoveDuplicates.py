class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return len(nums)
        tail = walker = 1
        while walker < len(nums):
            if nums[walker] != nums[tail - 1]:
                nums[tail] = nums[walker]
                tail += 1
            walker += 1
        return tail

