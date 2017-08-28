class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        localSum = [0 for i in range(len(triangle))]
        localSum[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            localSum[i] = localSum[i-1] + triangle[i][-1]
            for j in range(i-1, 0, -1):
                localSum[j] = min(localSum[j],localSum[j-1])+triangle[i][j]
            localSum[0] = localSum[0] + triangle[i][0]

        return min(localSum)