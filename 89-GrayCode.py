class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        size = 1 << n
        for i in range(0, size):
            res.append((i>>1)^i)

        return res