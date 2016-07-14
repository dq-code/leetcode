class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[0 for x in range(n)] for y in range(m)]
        matrix[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                up = 0
                if i - 1 >= 0:
                    up = matrix[i - 1][j]
                left = 0
                if j - 1 >= 0:
                    left = matrix[i][j - 1]
                matrix[i][j] = up + left
        return matrix[m - 1][n - 1]
