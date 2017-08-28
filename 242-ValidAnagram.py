class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False

        sortS = sorted(s)
        sortT = sorted(t)

        return sortS == sortT