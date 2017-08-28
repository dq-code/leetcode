class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_map = {0: -1}
        curSum = 0
        maxLen = 0
        for i in range(len(nums)):
            curSum += 1 if nums[i] == 1 else -1
            if curSum in len_map:
                maxLen = max(maxLen, i - len_map[curSum])
            else:
                len_map[curSum] = i

        return maxLen



