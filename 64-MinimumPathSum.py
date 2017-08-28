class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        matrix = [[ 0 for i in range(len(grid[0]))] for j in range(len(grid))]
        matrix[0][0] = grid[0][0]
        for i in range(1, len(matrix[0])):
            matrix[0][i] = matrix[0][i-1] + grid[0][i]

        for i in range(1, len(matrix)):
            matrix[i][0] = matrix[i-1][0] + grid[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1])+grid[i][j]

        return matrix[-1][-1]