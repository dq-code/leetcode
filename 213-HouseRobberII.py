class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        def helper(nums):
            odd = 0
            even = 0
            for i in range(len(nums)):
                if i % 2 == 0:
                    even = max(odd, even + nums[i])
                else:
                    odd = max(even, odd + nums[i])
            return max(even, odd)

        return max(helper(nums[0:-1]), helper(nums[1:]))