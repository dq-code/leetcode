class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        row = len(board)
        if row == 0: return
        col = len(board[0])
        queue = []

        def fill(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != 'O': return
            queue.append([r, c])
            board[r][c] = 'D'
            return

        def bfs(r, c):
            if board[r][c] == 'O':
                queue.append([r, c])
                fill(r, c)
            while len(queue) > 0:
                pair = queue.pop()
                i = pair[0]
                j = pair[1]
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j + 1)
                fill(i, j - 1)
            return

        for i in range(0, col):
            bfs(0, i)
            bfs(row - 1, i)

        for j in range(1, row - 1):
            bfs(j, 0)
            bfs(j, col - 1)

        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'D': board[i][j] = 'O'
                if board[i][j] == 'O': board[i][j] = 'X'

        return
