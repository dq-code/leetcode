class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in range(len(nums)):
            temp_sets = []
            for set in res:
                newSet = [nums[i]] + set
                newSet.sort()
                # print newSet
                if newSet not in res:
                    temp_sets.append(newSet)
            res += temp_sets

        return res
