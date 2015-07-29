class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        self.s = s
        self.lens = len(self.s)
        if self.lens == 0:
            return ""
        lp = self.s[0]
        for i in range(len(s)):
            subStr = self.helper(i, i)
            if len(subStr) > len(lp):
                lp = subStr
            print "index %i and lp now is %s"%(i, lp)
            if i+1<=self.lens-1:
                subStr = self.helper(i,i+1)
                if len(subStr) > len(lp):
                    lp = subStr
            print "index %i and lp now is %s"%(i, lp)
        return lp

    def helper(self, start1, start2):
        left = start1
        right = start2
        while left>=0 and right<self.lens and self.s[left] == self.s[right]:
            left = left - 1
            right = right + 1
        return self.s[left+1:right]

if __name__ == "__main__":
    input = "abb"
    runner =Solution()
    print runner.longestPalindrome(input)
            