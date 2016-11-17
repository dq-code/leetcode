class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s == '': return True

        map = [-1 for x in range(len(s) + 1)]
        map[0] = 0
        for i in range(1, len(s) + 1):
            for k in range(i):
                if map[k] >= 0 and s[k:i] in wordDict:
                    map[i] = k

        return map[len(s)] >= 0



