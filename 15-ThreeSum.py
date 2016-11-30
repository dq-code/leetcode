class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = []
        for i in range(len(nums)-2):
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target and [nums[i], nums[left], nums[right]] not in res:
                    res.append([nums[i], nums[left], nums[right]])
                elif sum > target:
                    right -= 1
                else:
                    left += 1


        return res