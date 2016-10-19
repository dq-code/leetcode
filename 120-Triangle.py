class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        matrix = [ 0 for x in range(len(triangle))]
        matrix[0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])-1, -1, -1):
                if j==0:
                    matrix[j] = matrix[j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    matrix[j] = matrix[j-1] + triangle[i][j]
                else:
                    matrix[j] = min(matrix[j],matrix[j-1])+triangle[i][j]

        return min(matrix)