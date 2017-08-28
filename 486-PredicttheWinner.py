class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        cache = {}
        def helper(nums):
            if len(nums)==1:
                return nums[0]
            tnums = tuple(nums)
            if tnums in cache:
                return cache[tnums]
            cache[tnums] = max(nums[0]-helper(nums[1:]), nums[-1]-helper(nums[0:-1]))
            return cache[tnums]

        return helper(nums)>=0