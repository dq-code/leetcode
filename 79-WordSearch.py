class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def helper(row, col, board, index):
            # print "row %d, col %d, index %d"%(row, col, index)
            # print board
            if index == len(word): return True

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                if newRow < 0 or newRow >= len(board) or newCol < 0 or newCol >= len(board[0]): continue
                if board[newRow][newCol] == word[index]:
                    board[newRow][newCol] = 0
                    if helper(newRow, newCol, board, index + 1): return True
                    board[newRow][newCol] = word[index]

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = 0
                    if helper(i, j, board, 1):
                        return True
                    board[i][j] = word[0]
        return False