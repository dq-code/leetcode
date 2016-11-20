class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i - 1] > nums[i]:
                break
            i += 1
        # print i
        if i == len(nums):
            return nums[0]
        return nums[i]
