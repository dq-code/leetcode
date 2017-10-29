from sets import Set


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        roots = [-1 for i in range(m * n)]
        res = []
        count = 0
        for x, y in positions:
            root = n * x + y
            roots[root] = root
            count += 1
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r, c = x + i, y + j
                cur_root = n * r + c
                if r < 0 or r >= m or c < 0 or c >= n or roots[cur_root] == -1: continue
                while cur_root != roots[cur_root]:
                    cur_root = roots[cur_root]
                if root != cur_root:
                    roots[root] = cur_root
                    count -= 1
                    root = cur_root
            res.append(count)
        return res

