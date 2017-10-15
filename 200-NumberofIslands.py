class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0

        number = 0
        rlen = len(grid)
        clen = len(grid[0])
        dirs = zip([1, 0, -1, 0], [0, 1, 0, -1])

        def helper(r, c):
            stack = [[r, c]]
            while stack:
                pos = stack.pop()
                grid[pos[0]][pos[1]] = 'x'
                for d in dirs:
                    nr = pos[0] + d[0]
                    nc = pos[1] + d[1]
                    if not (nr < 0 or nr >= rlen or nc < 0 or nc >= clen) and grid[nr][nc] != "0" and grid[nr][
                        nc] != 'x':
                        stack.append([nr, nc])

        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] != "0" and grid[i][j] != 'x':
                    helper(i, j)
                    number += 1
                else:
                    continue

        return number