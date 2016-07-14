class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        res = []

        row = 0
        col = 0
        printRow = True
        isIncrease = True
        while matrix[row][col] != 'x':
            res.append(matrix[row][col])
            matrix[row][col] = 'x'
            if printRow:
                if isIncrease:
                    col += 1
                    if col >= len(matrix[0]) or matrix[row][col] == 'x':
                        printRow = False
                        row += 1
                        col -= 1
                else:
                    col -= 1
                    if col < 0 or matrix[row][col] == 'x':
                        printRow = False
                        row -= 1
                        col += 1

            else:
                if isIncrease:
                    row += 1
                    if row >= len(matrix) or matrix[row][col] == 'x':
                        printRow = True
                        col -= 1
                        isIncrease = False
                        row -= 1
                else:
                    row -= 1
                    if row < 0 or matrix[row][col] == 'x':
                        printRow = True
                        col += 1
                        isIncrease = True
                        row += 1
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                break
        return res
