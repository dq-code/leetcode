class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = {}
        for i in range(len(s)):
            if s[i] in t:
