class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        res = []
        for item in nums:
            nums[abs(item) - 1] = - abs(nums[abs(item) - 1])

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res
