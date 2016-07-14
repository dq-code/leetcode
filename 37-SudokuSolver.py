class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def isValid(row, col):
            tmp = board[row][col]
            board[row][col] = 'A'
            for i in range(9):
                if board[row][i] == tmp:
                    return False
            for i in range(9):
                if board[i][col] == tmp:
                    return False
            subbox_row = (row / 3) * 3
            subbox_col = (col / 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[subbox_row + i][subbox_col + j] == tmp:
                        return False
            board[row][col] = tmp
            return True

        def helper():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i, j) and helper():
                                return True
                            else:
                                board[i][j] = '.'
                        return False
            return True

        helper()
