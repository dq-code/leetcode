class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(''.join([c.upper() for c in S]).split('-'))
        index = len(S)-1
        res = []
        while index>=0:
            if index+1 >= K:
                res.append(S[index-K+1:index+1])
                index = index - K
            else:
                res.append(S[:index+1])
                index = -1
        return '-'.join(res[::-1])