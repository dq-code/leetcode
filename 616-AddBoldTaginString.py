class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        queue = []
        res = ""
        mark = [False for i in range(len(s))]
        for i in range(len(s)):
            for w in dict:
                if s[i:].startswith(w):
                    mark[i:i + len(w)] = [True for j in range(i, i + len(w))]
        # print mark

        i = 0
        while i < len(s):
            if not mark[i]:
                res += s[i]
                i += 1
            else:
                word = ''
                while i < len(s) and mark[i]:
                    word += s[i]
                    i += 1
                res += '<b>' + word + '</b>'

        return res
