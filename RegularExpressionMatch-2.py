class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        source_len = len(s)

        pattern_ls = []
        for i in range(len(p)):
            if p[i] != '*':
                pattern_ls.append(p[i])
            else:
                pattern_ls[-1] += '*'
        pattern_len = len(pattern_ls)

        table = [[0 for x in range(source_len+1)] for x in range(pattern_len+1)]
        j = k = 0
        outofrange = False
        multi = False
        for j in range(pattern_len):
            if k in range(source_len):
                if '*' not in pattern_ls[j]:
                    if not multi:
                        if pattern_ls[j] == '.':
                            table[j+1][k+1] = table[j][k]+1
                        elif pattern_ls[j] == s[k]:
                            table[j+1][k+1] = table[j][k]+1
                        else:
                            return False
                    else:
                        i = k
                        no_match = True
                        while i < source_len:
                            if pattern_ls[j] == s[i] or pattern_ls[j] == '.':
                                index = max(table[j][i+1],table[j][i])
                                if index < i: table[j+1][i+1] = -1
                                elif table[j][i] == -1: table[j+1][i+1] = -1
                                else:
                                    table[j+1][i+1] = min(i+1, max(table[j][i],table[j][i+1])+1)
                                    if no_match:
                                        k = i
                                        no_match = False
                            else:
                                table[j+1][i+1] = -1
                            i += 1
                        if no_match: return False
                    k += 1
                if '*' in pattern_ls[j]:
                    multi = True
                    if pattern_ls[j][0] == '.':
                        for i in range(k, source_len):
                            table[j+1][i+1] = min(i+1, max(table[j][i], table[j+1][i], table[j][i+1])+1)
                    else:
                        i = k
                        while i<source_len:
                            if pattern_ls[j][0] == s[i] and i==max(table[j][i], table[j+1][i], table[j][i+1]):
                                table[j+1][i+1] = min(i+1, max(table[j][i], table[j+1][i], table[j][i+1])+1)
                            else:
                                table[j+1][i+1] = min(i+1, max(table[j][i], table[j][i+1]))
                            i += 1
            else:
                outofrange = True
                break

        #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in table]))
        match = True
        if outofrange:
            for i in range(j, pattern_len):
                if '*' in pattern_ls[i]:
                    for k in range(source_len+1):
                        table[i+1][k] = table[i][k]
                else:
                    match = False
                    break
        return table[pattern_len][source_len] >= source_len and match


if __name__ == "__main__":
    sl = Solution()
    print sl.isMatch('cbcaabcbaabccbaa','c*b*ab*.*b*c*a*')
