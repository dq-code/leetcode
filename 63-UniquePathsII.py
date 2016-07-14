class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        matrix = [[0 for x in range(col)] for y in range(row)]
        matrix[0][0] = 1
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                    continue
                if i == 0 and j == 0: continue
                up = 0
                if i - 1 >= 0:
                    up = matrix[i - 1][j]
                left = 0
                if j - 1 >= 0:
                    left = matrix[i][j - 1]
                matrix[i][j] = up + left
        # print matrix
        return matrix[-1][-1]
