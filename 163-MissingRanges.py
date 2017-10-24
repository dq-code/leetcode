class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower != upper:
                return [str(lower) + "->" + str(upper)]
            else:
                return [str(lower)]
        nums = [lower - 1] + nums + [upper + 1]
        res = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                start = nums[i - 1] + 1
                end = nums[i] - 1
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
        return res
