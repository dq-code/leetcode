class Solution(object):
    def isMatch(self, s, p):

        star_match = star = -1
        i = j = 0
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
                continue
            if j < len(p) and p[j] == '*':
                star = j
                star_match = i
                j += 1
                continue
            if star != -1:
                j = star + 1
                star_match += 1
                i = star_match
                continue
            return False

        if i < len(s):
            return False

        if j < len(p):
            for k in range(j, len(p)):
                if p[k] != '*':
                    return False
        return True
