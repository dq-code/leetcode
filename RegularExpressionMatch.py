class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        mark = 0
        matchAll = False
        i = 0
        while i in range(len(p)):
            if p[i] == "*":
                return False
            elif p[i] == ".":
                mark = mark+1
                if i+1 < len(p) and p[i+1] == "*":
                    if i+1 == len(p)-1:
                        return True
                    i = i+1
                    matchAll = True
            else:
                if matchAll:
                    found_ls = []
                    while mark in range(len(s)):
                        if p[i] == s[mark]:
                            found_ls.append(mark)
                        mark = mark+1
                    if len(found_ls)==0: return False
                    else:
                        res = False
                        for item in found_ls:
                            res = res or self.isMatch(s[item:],p[i:])
                        return res
                if i+1 < len(p) and p[i+1] == "*":
                    if mark not in range(len(s)) and i+1 == len(p)-1: return True
                    found_ls = []
                    index = mark
                    while index in range(len(s)):
                        if s[index] is not p[i]:
                            break
                        else:
                            found_ls.append(index)
                        index = index + 1
                    res=False
                    if len(found_ls) == 0:
                        i = i+2
                        continue
                    for item in found_ls:
                        if item+1 in range(len(s)):
                            res = res or self.isMatch(s[item+1:],p[i+2:])
                        else:
                            return True
                    return res
                elif mark not in range(len(s)) or s[mark] is not p[i]: return False
                mark=mark+1
            i = i+1
        if mark < len(s):
            return False
        return True

        