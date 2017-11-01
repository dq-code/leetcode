class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        row, col = len(rooms), len(rooms[0])

        queue = []
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append([i, j])

        while queue:
            r, c = queue.pop()
            cur = rooms[r][c]
            # print "row %d, col %d, val %d"%(r,c,cur)
            for d in dirs:
                new_r, new_c = r + d[0], c + d[1]
                if 0 <= new_r < row and 0 <= new_c < col and cur + 1 < rooms[new_r][new_c]:
                    # print "newr %d, newc %d"%(new_r, new_c)
                    rooms[new_r][new_c] = cur + 1
                    queue.append([new_r, new_c])





