class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        strList = s.split()
        for i in range(len(strList) - 1, -1, -1):
            res.append(strList[i])
        return ' '.join(res)
