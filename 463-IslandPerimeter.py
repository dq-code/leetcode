class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4
                    if i>0 and grid[i-1][j]:
                        res -= 2
                    if j>0 and grid[i][j-1]:
                        res-=2


        return res