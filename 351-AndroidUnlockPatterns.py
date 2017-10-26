class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = [[0 for i in range(10)] for j in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[7][9] = skip[9][7] = 8
        skip[3][9] = skip[9][3] = 6
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = skip[2][8] = skip[8][2] = 5

        def helper(visited, cur, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            visited[cur - 1] = True
            res = 0
            for i in range(9):
                if not visited[i] and (skip[cur][i + 1] == 0 or visited[skip[cur][i + 1] - 1]):
                    res += helper(visited, i + 1, remain - 1)
            visited[cur - 1] = False
            return res

        res = 0
        visited = [False for i in range(9)]
        for i in range(m, n + 1):
            res += helper(visited, 1, i - 1) * 4
            res += helper(visited, 4, i - 1) * 4
            res += helper(visited, 5, i - 1)

        return res

