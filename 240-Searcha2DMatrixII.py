class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        j = len(matrix[0]) - 1
        for i in range(len(matrix)):
            while j and matrix[i][j] > target:
                j -= 1
            if matrix[i][j] == target: return True

        return False