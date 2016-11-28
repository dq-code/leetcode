__author__ = 'qianden'
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.lstrip()
        if len(str) == 0 :
            return 0
        output = 0
        BASE = 10
        sign = 1
        if str[0] == "-":
            sign = -1
            str = str[1:]
        elif str[0] == "+":
            str = str[1:]
        for i in range(len(str)):
            diff = ord(str[i]) - ord("0")
            if diff >= 0 and diff < 10:
                output = output * BASE + diff
            else:
                break
        if output > 2147483647:
            output = 2147483647 if sign > 0 else 2147483648
        return output*sign


if __name__ == "__main__":
    input = -123
    print ord("0")
    #runner =Solution()
    #print runner.reverse(input)