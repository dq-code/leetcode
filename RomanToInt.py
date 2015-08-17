class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        int_ls = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_ls = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 0
        res = 0
        while i in range(len(s)):
            if i+1 in range(len(s)) and s[i:i+2] in roman_ls:
                #print s[i:i+2]
                res += int_ls[roman_ls.index(s[i:i+2])]
                i = i + 2
            else:
                #print s[i]
                res = res + int_ls[roman_ls.index(s[i])]
                i = i + 1
        return res

if __name__ == "__main__":
    input = "DCCCXC"
    runner = Solution()
    print runner.romanToInt(input)



