class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, rowIndex + 1):
            res.append([1 for x in range(i + 1)])
            for j in range(1, len(res[i - 1])):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res[rowIndex]
