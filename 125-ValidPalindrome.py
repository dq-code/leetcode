class Solution(object):
    def isAlpha(self, x):
        if (x >= 'a' and x <= 'z') or (x >= '0' and x <= '9') or (x >= 'A' and x <= 'Z'):
            return True
        return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "": return True
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and not self.isAlpha(s[i]):
                i += 1

            while j >= 0 and not self.isAlpha(s[j]):
                j -= 1

            if i >= len(s) and j >= 0:
                return False

            if i < len(s) and j < 0:
                return False

            if i >= len(s) and j < 0:
                break

            if s[i].title() != s[j].title():
                return False

            i += 1
            j -= 1
        return True
