class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maximum = 0

        i = 0
        while i < len(heights):
            if stack == [] or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()
                width = i if stack == [] else i - stack[-1] - 1
                area = width * heights[index]
                if maximum < area: maximum = area

        # print stack
        length = len(heights)
        while stack != []:
            index = stack.pop()
            width = length if stack == [] else length - stack[-1] - 1
            area = width * heights[index]
            if maximum < area: maximum = area

        return maximum
