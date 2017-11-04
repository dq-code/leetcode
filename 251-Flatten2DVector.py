class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec_list = vec2d
        self.cur_row = 0
        self.cur_col = 0
        self.total_row = len(self.vec_list)

    def next(self):
        """
        :rtype: int
        """
        res = self.vec_list[self.cur_row][self.cur_col]
        self.cur_col += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.cur_row < self.total_row:
            if self.cur_col < len(self.vec_list[self.cur_row]):
                return True
            self.cur_col = 0
            self.cur_row += 1
        return False


        # Your Vector2D object will be instantiated and called as such:
        # i, v = Vector2D(vec2d), []
        # while i.hasNext(): v.append(i.next())