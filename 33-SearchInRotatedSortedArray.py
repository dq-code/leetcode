class Solution(object):
    def __init__(self):
        self.nums = []
        self.target = 0

    def helper(self, start, end, rotate_pos):
        total_len = len(self.nums)
        if (end - rotate_pos + total_len) % total_len < (start - rotate_pos + total_len) % total_len:
            return -1
        if start == end:
            if self.nums[start] == self.target:
                return start
            else:
                return -1

        length = (end - rotate_pos + total_len) % total_len - (start - rotate_pos + total_len) % total_len + 1
        mid = (start + length / 2) % total_len
        if self.target == self.nums[mid]:
            return mid
        elif self.target < self.nums[mid]:
            if start == mid: return -1
            return self.helper(start, (mid - 1 + total_len) % total_len, rotate_pos)
        else:
            if mid == end: return -1
            return self.helper((mid + 1) % total_len, end, rotate_pos)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        self.nums = nums
        self.target = target

        max_index = 0

        i = 1
        while i < len(self.nums):
            if self.nums[i] < self.nums[max_index]: break
            max_index = i
            i += 1

        rotate_pos = (max_index + 1) % len(self.nums)

        return self.helper(rotate_pos, max_index, rotate_pos)
