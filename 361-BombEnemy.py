class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        max_e = 0

        def helper(r, c):
            enemy = 0
            start, end = c - 1, c + 1
            while start >= 0 and grid[r][start] != 'W':
                if grid[r][start] == 'E':
                    enemy += 1
                start -= 1
            while end < len(grid[0]) and grid[r][end] != 'W':
                if grid[r][end] == 'E':
                    enemy += 1
                end += 1
            start, end = r - 1, r + 1
            while start >= 0 and grid[start][c] != 'W':
                if grid[start][c] == 'E':
                    enemy += 1
                start -= 1
            while end < len(grid) and grid[end][c] != 'W':
                if grid[end][c] == 'E':
                    enemy += 1
                end += 1
            # print enemy
            return enemy

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    max_e = max(max_e, helper(i, j))
        return max_e