class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        map = [[False for x in range(len(p) + 1)] for y in range(len(s) + 1)]
        map[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                map[0][i] = map[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    map[i][j] = map[i - 1][j - 1]
                elif p[j - 1] == '*':
                    map[i][j] = map[i][j - 1] or map[i][j - 2] or (
                    map[i - 1][j] and (p[j - 2] == '.' or s[i - 1] == p[j - 2]))
                else:
                    map[i][j] = map[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return map[len(s)][len(p)]
