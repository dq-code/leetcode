class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        res = 0
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                res = 1

        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                res = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        # print dp
        return res * res