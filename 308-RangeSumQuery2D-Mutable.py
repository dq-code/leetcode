class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        self.matrix = matrix
        self.colsums = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(len(matrix[0])):
                self.colsums[i][j] = self.colsums[i - 1][j] + self.matrix[i - 1][j]
                # print self.colsums

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        for i in range(row + 1, len(self.colsums)):
            self.colsums[i][col] += diff
        self.matrix[row][col] = val
        # print self.colsums

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(col1, col2 + 1):
            res += self.colsums[row2 + 1][i] - self.colsums[row1][i]
        return res



        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # obj.update(row,col,val)
        # param_2 = obj.sumRegion(row1,col1,row2,col2)