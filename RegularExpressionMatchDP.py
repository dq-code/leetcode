class Solution:
    def isMatch(self, s, p):
        matrix = [[False for x in range(len(p)+1)] for x in range(len(s)+1)]
        matrix[0][0] = True
        for i in range(len(p)):
            if p[i] is "*" and i-1>=0:
                matrix[0][i+1] = matrix[0][i-1]
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] is "*" and j-1>=0:
                    if p[j-1] is s[i] or p[j-1] is ".":
                        matrix[i+1][j+1] = matrix[i][j+1]
                    matrix[i+1][j+1] = matrix[i+1][j+1] or matrix[i+1][j-1] or matrix[i+1][j]
                elif p[j] is ".":
                    matrix[i+1][j+1] = matrix[i][j]
                else:
                    matrix[i+1][j+1] = matrix[i][j] and (p[j] == s[i])
        return matrix[len(s)][len(p)]

if __name__ == "__main__":
    input = "aab"
    pattern = "c*a*b"
    runner =Solution()
    print runner.isMatch(input, pattern)
