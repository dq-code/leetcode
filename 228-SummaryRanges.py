class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []

        res = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                res[-1][1] = nums[i - 1]
                res.append([nums[i], nums[i]])
            else:
                res[-1][1] = nums[i]
        return [str(r[0])+'->'+str(r[1]) if r[0]!=r[1] else str(r[0]) for r in res]