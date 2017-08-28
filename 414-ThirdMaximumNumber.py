class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        walker = len(nums) - 2
        rank = 1
        while walker >= 0:
            if nums[walker] < nums[walker + 1]:
                rank += 1
            if rank == 3:
                break
            walker -= 1
        return nums[walker] if rank == 3 else nums[-1]
