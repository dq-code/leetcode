class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = end = 0
        shortDist = len(nums) + 1
        curSum = 0
        while end < len(nums):
            while end < len(nums) and curSum < s:
                curSum += nums[end]
                end += 1
            while start < end and curSum >= s:
                shortDist = min(shortDist, end - start)
                curSum -= nums[start]
                start += 1

        return shortDist if shortDist < len(nums) + 1 else 0