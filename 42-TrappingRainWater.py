class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        leftHighestLs = [0 for x in range(len(height))]
        total = rightHighest = 0
        if len(height) == 0: return 0
        leftHighestLs[0] = height[0]
        for i in range(1, len(height)):
            if height[i] > leftHighestLs[i - 1]:
                leftHighestLs[i] = height[i]
            else:
                leftHighestLs[i] = leftHighestLs[i - 1]
        for i in range(len(height) - 1, 0, -1):
            if height[i] > rightHighest:
                rightHighest = height[i]
            if min(leftHighestLs[i], rightHighest) > height[i]:
                total += min(leftHighestLs[i], rightHighest) - height[i]

        return total
