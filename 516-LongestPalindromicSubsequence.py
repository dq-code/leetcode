class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # matrix = [[0 for x in range(len(s))] for y in range(len(s))]
        # for i in range(len(s)-1, -1, -1):
        #     matrix[i][i] = 1
        #     for j in range(i+1, len(s)):
        #         if s[i]==s[j]:
        #             matrix[i][j] = matrix[i+1][j-1]+2
        #         else:
        #             matrix[i][j] = max(matrix[i+1][j], matrix[i][j-1])
        #
        # return matrix[0][-1]
        dp = [0 for j in range(len(s))]
        for i in range(1, len(s)):
            dp[i] = 1
            prev = 0
            for j in range(i-1, -1, -1):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j+1], dp[j])
                prev = tmp
        return dp[0]
