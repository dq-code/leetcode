class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        mark = 0
        while i >= 0:
            if nums[i + 1] > nums[i]:
                j = len(nums) - 1
                while j > i:
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        mark = i + 1
                        break
                    j -= 1
                break
            i -= 1

        i = mark
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
