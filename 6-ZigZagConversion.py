class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [[] for i in range(numRows)]
        row = 0
        down = True
        for i in range(len(s)):
            res[row].append(s[i])
            if numRows > 1:
                if row == numRows - 1:
                    down = False
                if row == 0:
                    down = True
                if down:
                    row += 1
                else:
                    row -= 1

        resStr = ''
        for ls in res:
            resStr += ''.join(ls)
        return resStr
