class Solution(object):
    def noFight(self, row, col, board):
        i = row - 1
        j = col - 1
        k = col + 1
        while i >= 0:
            if board[i][col] == 'Q': return False
            if j >= 0 and board[i][j] == 'Q': return False
            if k < self.n and board[i][k] == 'Q': return False
            i -= 1
            j -= 1
            k += 1
        return True

    def helper(self, row, board):
        if row == self.n:
            board_update = []
            for row in board:
                board_update.append(''.join(row))
            self.res.append(board_update)
            # print board_update
            return
        i = 0
        while i < self.n:
            if self.noFight(row, i, board):
                board[row][i] = 'Q'
                self.helper(row + 1, board)
                board[row][i] = '.'
            i += 1
        return

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.res = []
        board = [['.' for x in range(n)] for y in range(n)]

        self.helper(0, board)
        return self.res
