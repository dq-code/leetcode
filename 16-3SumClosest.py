class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        minDiff = 100000
        res = -1
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = target - sum
                if diff == 0:
                    return sum
                if abs(diff) < minDiff:
                    minDiff = abs(diff)
                    res = sum
                if diff < 0:
                    right = right - 1
                else:
                    left = left + 1
        return res
