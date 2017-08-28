class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = des = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                inc = des + 1
            if nums[i] < nums[i-1]:
                des = inc+1
        return max(inc,des)