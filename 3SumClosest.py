class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0
        nums = sorted(nums, key=int)
        diff = 9999
        mark = 1
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    diff_t = target - sum
                    if diff_t == 0:
                        return sum
                    if abs(diff_t) < diff:
                        diff = abs(diff_t)
                        mark = 1 if diff_t > 0 else -1
                    if diff_t < 0:
                        while left<right:
                            right = right - 1
                            if nums[right] < nums[right+1]: break
                    if diff_t > 0:
                        while left<right:
                            left = left + 1
                            if nums[left] > nums[left-1]: break

        return target - diff_t*mark