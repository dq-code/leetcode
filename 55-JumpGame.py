class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        curMax = 0
        for i in len(nums):
            if curMax < i: return False
            curMax = max(curMax, i + nums[i])

        return True
