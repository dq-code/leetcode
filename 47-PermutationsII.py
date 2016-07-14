class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]: continue
            else:
                for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                    res.append([nums[i]]+j)

        return res