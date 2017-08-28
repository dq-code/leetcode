import collections
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        twice = collections.Counter(nums).most_common(1)[0][0]
        res.append(twice)
        lost = (1+len(nums))*len(nums)/2 - sum(nums) + twice
        res.append(lost)
        return res