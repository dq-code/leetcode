class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # matrix = [[0 for i in range(len(s))] for j in range(len(s))]
        #
        # for i in range(len(s)):
        #     matrix[i][i] = 1
        #
        # for i in range(1, len(s)):
        #     if s[i] == s[i-1]:
        #         matrix[i-1][i] = 1
        #
        # for i in range(3, len(matrix)):
        #     for j in range(0, len(s)-i+1):
        #         end = j+i-1
        #         if s[j]==s[end] and matrix[j+1][end-1]==1:
        #             matrix[j][end]=1
        #
        #
        # return sum([sum(ll) for ll in matrix])