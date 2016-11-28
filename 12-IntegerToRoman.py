class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        roman = ''
        while num > 0:
            i = 0
            while i in range(len(values)):
                res = num/values[i]
                if res > 0:
                    for j in range(num/values[i]):
                        roman += numerals[i]
                    num = num%values[i]
                    break
                i += 1
        return roman