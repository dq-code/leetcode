class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        palindromeCut = [0 for x in range(len(s)+1)]
        palindromeCut[len(s)] = 0
        palindromeCut[len(s)-1] = 0

        matrix = [[False for x in range(len(s))] for y in range(len(s))]


        for i in range(len(s)-2, -1, -1):
            minCut = len(s)
            for j in range(i, len(s)):
                if s[j]==s[i] and (i-j<2 or matrix[j+1][i-1]):
                    matrix[j][i] = True
                    minCut = min(minCut, palindromeCut[j+1]+1)
            palindromeCut[i] = minCut

        return palindromeCut[0]