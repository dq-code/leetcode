class Solution(object):
    def helper(self, start, end, nums, target):
        if start < 0 or end >= len(nums):
            return [-1, -1]

        length = end - start + 1
        mid = start + length / 2
        if nums[mid] == target:
            end = start = i = mid
            while i - 1 >= 0:
                if nums[i - 1] == target:
                    i -= 1
                else:
                    break
            start = i
            i = mid
            while i + 1 < len(nums):
                if nums[i + 1] == target:
                    i += 1
                else:
                    break
            end = i
            return [start, end]
        elif nums[mid] > target:
            if mid - 1 >= start:
                res = self.helper(start, mid - 1, nums, target)
                if res != [-1, -1]: return res
        else:
            if mid + 1 <= end:
                res = self.helper(mid + 1, end, nums, target)
                if res != [-1, -1]: return res

        return [-1, -1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        return self.helper(0, len(nums) - 1, nums, target)
