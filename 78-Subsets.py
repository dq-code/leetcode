class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(comb, nums, k):
            if k < 0: return
            res.append(comb)
            for i in range(len(nums)):
                helper(comb + [nums[i]], nums[i + 1:], k - 1)

        k = len(nums)
        res = []
        helper([], nums, k)
        return res
