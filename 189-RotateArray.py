class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        realK = k%len(nums)
        self.helper(nums, 0, len(nums)-1)
        self.helper(nums, 0, realK-1)
        self.helper(nums,realK, len(nums)-1)

    def helper(self, nums, start, end):
        left = start
        right = end
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

