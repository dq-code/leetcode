class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != len(board[0]) and len(board) != 9:
            return False

        i = 0
        for i in range(9):
            row_hash = [0] * 9
            for j in range(9):
                if board[i][j] != '.':
                    decoded_num = ord(board[i][j]) - ord('1')
                    if row_hash[decoded_num] == 1:
                        return False
                    else:
                        row_hash[decoded_num] = 1

                if i % 3 == 0 and j % 3 == 0:
                    subbox_hash = [0] * 9
                    for m in range(3):
                        for n in range(3):
                            if board[i + m][j + n] != '.':
                                decoded_num = ord(board[i + m][j + n]) - ord('1')
                                if subbox_hash[decoded_num] == 1:
                                    return False
                                else:
                                    subbox_hash[decoded_num] = 1

        for j in range(9):
            col_hash = [0] * 9
            for i in range(9):
                if board[i][j] != '.':
                    decoded_num = ord(board[i][j]) - ord('1')
                    if col_hash[decoded_num] == 1:
                        return False
                    else:
                        col_hash[decoded_num] = 1

        return True
