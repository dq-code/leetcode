class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2: return nums

        prev = 1
        cur = 2
        while cur < len(nums):
            if nums[prev] == nums[cur] and nums[prev-1] == nums[cur]:
                cur += 1
            else:
                prev += 1
                nums[prev] = nums[cur]
                cur += 1
        return prev + 1
