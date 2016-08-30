class Solution(object):
    def calculateLatestRectangle(self, heights):
        # print heights
        maxium_area = 0
        stack = []
        i = 0
        length = len(heights)
        while i < length:
            if len(stack) == 0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()
                width = i if len(stack) == 0 else i - stack[-1] - 1
                maxium_area = max(maxium_area, width * heights[index])
        while len(stack) > 0:
            index = stack.pop()
            width = length if len(stack) == 0 else length - stack[-1] - 1
            maxium_area = max(maxium_area, width * heights[index])

        return maxium_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []: return 0

        histogram = [0 for i in range(len(matrix[0]))]
        maxium_area = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                histogram[j] = histogram[j] + 1 if matrix[i][j] == '1' else 0

            maxium_area = max(maxium_area, self.calculateLatestRectangle(histogram))

        return maxium_area
