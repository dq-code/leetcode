class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        res = []
        row = col = 0
        dir = 0
        while len(res) < len(matrix)*len(matrix[0]):
            res.append(matrix[row][col])
            matrix[row][col] = 'x'
            tempRow = row+directions[dir][0]
            tempCol = col + directions[dir][1]
            if tempRow<0 or tempRow>=len(matrix) or tempCol<0 or tempCol>=len(matrix[0]) or matrix[tempRow][tempCol] == 'x':
                dir += 1
                dir = dir%4
                tempRow = row + directions[dir][0]
                tempCol = col + directions[dir][1]
            row = tempRow
            col = tempCol

        return res
