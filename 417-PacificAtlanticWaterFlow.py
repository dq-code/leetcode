class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        pacific = [[False for i in range(n)] for j in range(m)]
        atlantic = [[False for i in range(n)] for j in range(m)]

        def dfs(r, c, visited):
            visited[r][c] = True
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for i, j in dirs:
                new_r, new_c = r + i, c + j
                if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n or visited[new_r][new_c] or matrix[r][c] > \
                        matrix[new_r][new_c]:
                    continue
                dfs(new_r, new_c, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for i in range(n):
            dfs(0, i, pacific)
            dfs(m - 1, i, atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

