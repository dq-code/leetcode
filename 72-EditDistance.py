class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if len(word1) == 0 and len(word2) != 0: return len(word2)
        if len(word1) != 0 and len(word2) == 0: return len(word1)
        if len(word1) == 0 and len(word2) == 0: return 0

        matrix = [[0 for x in range(len(word2))] for y in range(len(word1))]

        matrix[0][0] = 1 if word1[0] != word2[0] else 0
        for i in range(1, len(word2)):
            matrix[0][i] = i if word1[0] == word2[i] else matrix[0][i - 1] + 1
        for i in range(1, len(word1)):
            matrix[i][0] = i if word1[i] == word2[0] else matrix[i - 1][0] + 1
        # print matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                diag = matrix[i - 1][j - 1] if word2[j] == word1[i] else matrix[i - 1][j - 1] + 1
                up = matrix[i - 1][j] + 1
                left = matrix[i][j - 1] + 1
                matrix[i][j] = min(diag, up, left)

        return matrix[-1][-1]
