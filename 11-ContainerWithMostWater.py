class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if len(height) is 0:
            return 0
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            storage = min(height[left], height[right]) * (left - right)
            res = storage if res < storage else res
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return res
