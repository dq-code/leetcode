class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = ['0', '1', '8'] if n % 2 else ['']
        while n > 1:
            n -= 2
            res = [a + num + b for a, b in ['00', '11', '88', '69', '96'][n < 2:] for num in res]
        return res
