import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        sortKeys = sorted(counter.keys())
        maxLen = 0
        for i in range(1, len(sortKeys)):
            if sortKeys[i] - sortKeys[i - 1] == 1:
                maxLen = max(maxLen, counter[sortKeys[i]] + counter[sortKeys[i - 1]])

        return maxLen
