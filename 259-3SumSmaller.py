class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: 0
        res = 0
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] < target:
                    res += end - start
                    start += 1
                else:
                    end -= 1
        return res
