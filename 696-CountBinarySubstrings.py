class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        groups = []
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                groups.append(cur)
                cur = 1
        groups.append(cur)

        # print groups
        res = 0
        for i in range(1, len(groups)):
            res += min(groups[i], groups[i - 1])
        return res

