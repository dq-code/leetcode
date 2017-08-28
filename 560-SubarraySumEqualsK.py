class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subSum = {}
        subSum[0] = 1
        curSum = 0
        res = 0
        for i in range(len(nums)):
            curSum += nums[i]
            residue = curSum - k
            if residue in subSum:
                res += subSum[residue]
            if curSum in subSum:
                subSum[curSum] += 1
            else:
                subSum[curSum] = 1

        return res