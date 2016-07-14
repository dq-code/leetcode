class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        n -= 1
        while n > 0:
            temp = res
            res = ''
            count = 1
            prev = temp[0]
            for i in range(1, len(temp)):
                if temp[i] == prev:
                    count += 1
                else:
                    res += str(count) + prev
                    count = 1
                prev = temp[i]
            res += str(count) + prev
            n -= 1
        return res
