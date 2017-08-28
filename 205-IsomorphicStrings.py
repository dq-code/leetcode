class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t): return False
        char_map = {}
        index = 0
        while index < len(s) and index < len(t):
            if s[index] not in char_map:
                if t[index] in char_map.values():
                    return False
                char_map[s[index]] = t[index]
            else:
                if char_map[s[index]] != t[index]:
                    return False
            index += 1

        return True