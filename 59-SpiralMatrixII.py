class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for x in range(n)] for y in range(n)]

        if n==0:
            return matrix

        isRow = True
        isIncreae = True
        curValue = 1
        row = 0
        col = 0

        maxium = n*n

        while curValue<=maxium:
            matrix[row][col] = curValue
            curValue += 1

            if isRow:
                if isIncreae:
                    col += 1
                    if col>=n or matrix[row][col]>0:
                        row += 1
                        col -= 1
                        isRow = False
                else:
                    col -= 1
                    if col < 0 or matrix[row][col]>0:
                        row -= 1
                        col += 1
                        isRow = False

            else:
                if isIncreae:
                    row += 1
                    if row >= n or matrix[row][col]>0:
                        col -= 1
                        row -= 1
                        isRow = True
                        isIncreae = False
                else:
                    row -= 1
                    if row < 0 or matrix[row][col]>0:
                        col += 1
                        row += 1
                        isRow = True
                        isIncreae = True
            if row < 0 or row >= n or col < 0 or col >= n:
                break

        return matrix

