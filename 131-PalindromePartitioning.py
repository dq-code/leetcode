class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def isPalindrome(s):
            i = 0
            j = len(s)-1
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def helper(s, strList):
            if len(s) == 0:
                res.append(strList)
            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]):
                    helper(s[i:], strList+[s[:i]])

        helper(s, [])
        return res