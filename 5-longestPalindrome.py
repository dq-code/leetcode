class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return s[l + 1:r]

        palindrome = ''
        for i in range(len(s)):
            res = isPalindrome(i, i)
            if len(res) > len(palindrome):
                palindrome = res
            res = isPalindrome(i, i + 1)
            if len(res) > len(palindrome):
                palindrome = res
        return palindrome
