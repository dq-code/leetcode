class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        visited = [[False for i in range(n)] for j in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        max_path = 0

        def dfs(r, c):
            if visited[r][c]: visited[r][c]
            visited[r][c] = 1
            cur_path = 0
            for i, j in dirs:
                new_r, new_c = r + i, c + j
                if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n or matrix[new_r][new_c] <= matrix[r][c]:
                    continue
                if visited[new_r][new_c]:
                    cur_path = max(cur_path, visited[new_r][new_c])
                else:
                    cur_path = max(cur_path, dfs(new_r, new_c))
            visited[r][c] = cur_path + 1
            return visited[r][c]

        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))
        return max_path

