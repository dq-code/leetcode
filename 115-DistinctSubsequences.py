class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        matrix = [[0 for x in range(len(t) + 1)] for y in range(len(s) + 1)]
        for i in range(len(s) + 1):
            matrix[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, min(i + 1, len(t) + 1)):
                if s[i - 1] == t[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j]

        return matrix[len(s)][len(t)]
