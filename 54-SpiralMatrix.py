class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = 0, 0
        d = 0
        res = []
        while True:
            res.append(matrix[r][c])
            matrix[r][c] = 'x'
            visited = [d]
            all_visited = False
            while True:
                nr, nc = r + dirs[d][0], c + dirs[d][1]
                if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[0]) or matrix[nr][nc] == 'x':
                    d = (d + 1) % 4
                    if d not in visited:
                        visited.append(d)
                    else:
                        all_visited = True
                        break
                else:
                    r, c = nr, nc
                    break
            if all_visited: break
        return res