class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                up = -1
                if i - 1 >= 0:
                    up = grid[i - 1][j]
                left = -1
                if j - 1 >= 0:
                    left = grid[i][j - 1]

                if up >= 0 and left >= 0:
                    grid[i][j] = min(up, left) + grid[i][j]
                else:
                    grid[i][j] = up + grid[i][j] if up >= 0 else left + grid[i][j]

        return grid[-1][-1]
