class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums = sorted(nums, key=int)
        res = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1
                right = len(nums)-1
                residue = 0 - nums[i]
                while i+1 in range(len(nums)) and left < right:
                    sum = nums[left] + nums[right]
                    if sum == residue:
                        triplet = [nums[i], nums[left], nums[right]]
                        res.append(triplet)
                        left = left + 1
                        right = right - 1
                        while left<right and nums[left] == nums[left-1]: left = left + 1
                        while left<right and nums[right] == nums[right+1]: right = right - 1
                    elif sum < residue:
                        while left < right:
                            left = left + 1
                            if nums[left] > nums[left-1]: break
                    else:
                        while left < right:
                            right = right - 1
                            if nums[right] < nums[right+1]: break
        return res