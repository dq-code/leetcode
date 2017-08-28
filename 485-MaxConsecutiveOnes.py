class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        curCount = 0
        for item in nums:
            if item == 1:
                curCount += 1
            else:
                maxCount = curCount if curCount > maxCount else maxCount
                curCount = 0
        maxCount = curCount if curCount > maxCount else maxCount

        return maxCount
