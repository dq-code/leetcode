class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        p = self.simplifyPattern(p)
        #print "after simplify %s"%p
        mark = 0
        matchAll = False
        i = 0
        while i in range(len(p)):
            if p[i] == "*":
                return False
            elif p[i] == ".":
                if matchAll:
                    res = False
                    index = mark
                    while index in range(len(s)):
                        res = res or self.isMatch(s[index:],p[i:])
                        index = index + 1
                    return res
                if i+1 < len(p) and p[i+1] == "*":
                    if i+1 == len(p)-1:
                        return True
                    i = i+1
                    matchAll = True
                elif mark not in range(len(s)): return False
                else:
                    mark = mark + 1
            else:
                if matchAll:
                    match_map = {}
                    match_map[i] = p[i]
                    look_up = i
                    star_ele = True
                    while look_up in range(len(p)) and star_ele:
                        if look_up+1 in range(len(p)) and p[look_up+1] == "*":
                            match_map[look_up] = p[look_up]
                            look_up = look_up + 2
                        else:
                            star_ele = False
                    if look_up in range(len(p)): match_map[look_up] = p[look_up]
                    else: return True
                    index = mark
                    while index in range(len(s)):
                        if "." in match_map.values():
                            for key in match_map.keys():
                                if match_map[key] == ".":
                                    if self.isMatch(s[index:],p[key:]): return True
                        if s[index] in match_map.values():
                            for key in match_map.keys():
                                if s[index] == match_map[key]:
                                    if self.isMatch(s[index:],p[key:]): return True
                        index += 1
                    return False
                if i+1 < len(p) and p[i+1] == "*":
                    index = mark
                    while index in range(len(s)):
                        if s[index] is not p[i]:
                            break
                        index = index + 1
                    k = index
                    if i+2 in range(len(p)):
                        while k >= mark:
                            if self.isMatch(s[k:],p[i+2:]): return True
                            k = k - 1
                        return False
                    elif i+2 not in range(len(p)):
                        return index == len(s)
                elif mark not in range(len(s)) or s[mark] is not p[i]: return False
                mark = mark+1
            i = i+1
        if mark < len(s):
            return False
        return True

    def simplifyPattern(self, p):
        i = 0
        orig_len = len(p)
        while i in range(orig_len):
            if i not in range(len(p)):
                break
            if p[i] != "*":
                if i+1 in range(len(p)) and p[i+1]=="*":
                    index = i+2
                    new_len = len(p)
                    while index+1 in range(new_len):
                        if index+1 not in range(len(p)): break
                        if p[index:index+2] == "%s*"%p[i]:
                            p = p[:index]+p[index+2:]
                            continue
                        else: break
            i = i+1
        return p


if __name__ == "__main__":
    input = "aabcbcbcaccbcaabc"
    pattern = ".*a*aa*.*b*.c*.*a*"
    runner =Solution()
    print runner.isMatch(input, pattern)