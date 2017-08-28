class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)
        comb1 = nums[-1] * nums[-2] * nums[-3]
        comb2 = nums[0] * nums[1] * nums[-1]
        comb3 = nums[-1] * nums[-2] * nums[0]

        return max(comb1, comb2, comb3)
