class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        len_row = len(board)
        len_col = len(board[0])

        def countLive(row, col):
            dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            live = 0
            for d in dirs:
                check_row = row + d[0]
                check_col = col + d[1]
                if check_row < 0 or check_row >= len_row or check_col < 0 or check_col >= len_col:
                    continue
                else:
                    if type(board[check_row][check_col]) is tuple:
                        live += board[check_row][check_col][0]
                    else:
                        live += board[check_row][check_col]
            return live

        for i in range(len_row):
            for j in range(len_col):
                live_num = countLive(i, j)
                if live_num < 2:
                    board[i][j] = (board[i][j], 0)
                elif live_num == 3 and not board[i][j]:
                    board[i][j] = (board[i][j], 1)
                elif live_num > 3:
                    board[i][j] = (board[i][j], 0)
                else:
                    board[i][j] = (board[i][j], board[i][j])

        for i in range(len_row):
            for j in range(len_col):
                board[i][j] = board[i][j][1]



