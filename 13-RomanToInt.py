class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        res = 0
        while i in range(len(s)):
            j = 0
            for j in range(len(numerals)):
                if len(numerals[j]) == 2 and s[i:i + 2] == numerals[j]:
                    res += values[j]
                    i += 2
                    break
                if len(numerals[j]) == 1 and s[i:i + 1] == numerals[j]:
                    res += values[j]
                    i += 1
                    break
                j += 1
        return res
