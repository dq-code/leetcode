class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsNew = sorted(nums)
        start = end = -1
        for i in range(len(nums)):
            if nums[i] != numsNew[i]:
                if start == -1: start = i
                end = i
        return 0 if start == end else end - start + 1
