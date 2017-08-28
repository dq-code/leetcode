class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        matrix = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        matrix[0][0] = 1

        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                matrix[0][i] = 0
            else:
                matrix[0][i] = matrix[0][i - 1]

        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                matrix[i][0] = 0
            else:
                matrix[i][0] = matrix[i - 1][0]

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[-1][-1]