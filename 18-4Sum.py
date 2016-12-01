class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                newTarget = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[left] + nums[right]
                    if sum == newTarget and [nums[i], nums[j], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left = left + 1
                        right = right - 1
                    elif sum < newTarget:
                        left = left + 1
                    else:
                        right = right - 1

        return res
