class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum(sorted(nums)[::2])
#array[start:stop:step]