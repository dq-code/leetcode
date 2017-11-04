class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memory = {}
        def helper(s):
            i = 0
            if s in memory: return memory[s]
            while i<len(s):
                if s[i:i+2]=='++' and not helper(s[:i]+'--'+s[i+2:]):
                    memory[s] = True
                    return True
                i += 1
            return False
        return helper(s)