class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        firstLetter = word[0]
        firstLetterList = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == firstLetter:
                    firstLetterList.append([i, j])

        def helper(pos, i):
            if i == len(word): return True

            if pos[0] - 1 >= 0 and board[pos[0] - 1][pos[1]] == word[i]:
                temp = board[pos[0] - 1][pos[1]]
                board[pos[0] - 1][pos[1]] = 0
                if helper([pos[0] - 1, pos[1]], i + 1): return True
                board[pos[0] - 1][pos[1]] = temp
            if pos[0] + 1 < len(board) and board[pos[0] + 1][pos[1]] == word[i]:
                temp = board[pos[0] + 1][pos[1]]
                board[pos[0] + 1][pos[1]] = 0
                if helper([pos[0] + 1, pos[1]], i + 1): return True
                board[pos[0] + 1][pos[1]] = temp
            if pos[1] - 1 >= 0 and board[pos[0]][pos[1] - 1] == word[i]:
                temp = board[pos[0]][pos[1] - 1]
                board[pos[0]][pos[1] - 1] = 0
                if helper([pos[0], pos[1] - 1], i + 1): return True
                board[pos[0]][pos[1] - 1] = temp
            if pos[1] + 1 < len(board[0]) and board[pos[0]][pos[1] + 1] == word[i]:
                temp = board[pos[0]][pos[1] + 1]
                board[pos[0]][pos[1] + 1] = 0
                if helper([pos[0], pos[1] + 1], i + 1): return True
                board[pos[0]][pos[1] + 1] = temp

            return False

        for pair in firstLetterList:
            temp = board[pair[0]][pair[1]]
            board[pair[0]][pair[1]] = 0
            if helper(pair, 1): return True
            board[pair[0]][pair[1]] = temp
        return False
