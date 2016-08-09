class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            hasZero = False
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    hasZero = True
                    matrix[i][j] = 'ZERO'
            if hasZero:
                for j in range((len(matrix[0]))):
                    if matrix[i][j] != 'ZERO': matrix[i][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'ZERO':
                    for k in range((len(matrix))):
                        matrix[k][j] = 0
