class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        source_len = len(s)
        if source_len<=0: return False

        pattern_ls = []
        for i in range(len(p)):
            if p[i] != '*':
                pattern_ls.append(p[i])
            else:
                pattern_ls[-1] += '*'

        pattern_len = len(pattern_ls)
        print pattern_ls
        table = [[0 for x in range(source_len+1)] for x in range(pattern_len+1)]
        k = 0
        for j in range(pattern_len):
            if k in range(source_len):
                if '*' not in pattern_ls[j]:
                    if j==0 or '*' not in pattern_ls[j-1]:
                        if pattern_ls[j] == '.':
                            table[j+1][k+1] = table[j][k]+1
                        elif pattern_ls[j] == s[k]:
                            table[j+1][k+1] = table[j][k]+1
                        else:
                            table[j+1][k+1] = -1
                        k+=1
                    else:
                        i = k
                        while(i < source_len):
                            if pattern_ls[j] == '.':
                                table[j+1][i+1] = table[j][i]+1
                            elif pattern_ls[j] == s[i]:
                                table[j+1][i+1] = table[j][i]+1
                            else:
                                table[j+1][i+1] = -1
                            i += 1
                if '*' in pattern_ls[j]:
                    if pattern_ls[j][0] == '.':
                        table[j+1][k+1] = max(table[j][k], table[j+1][k], table[j][k+1])+1
                        for i in range(k+1, source_len):
                            table[j+1][i+1] = table[j+1][i] + 1
                    else:
                        i = 0
                        while(i<k):
                            print "enter"
                            table[j+1][i+1] = max(table[j][i], table[j+1][i], table[j][i+1])
                            i += 1
                        while(i<source_len):
                            if pattern_ls[j][0] == s[i]:
                                table[j+1][i+1] = max(table[j][i], table[j+1][i], table[j][i+1]) + 1
                            else:
                                #print "not equal, %d,%d,%d"%(table[j][i], table[j+1][i], table[j][i+1])
                                table[j+1][i+1] = max(table[j][i], table[j+1][i], table[j][i+1])
                            i += 1

        print table
        if j < pattern_len:
            flag = True
            for i in range(pattern_len):
                if '*' not in pattern_ls[i]: flag = False
            if(flag): table[pattern_len][source_len] = table[j][source_len]
        return table[pattern_len][source_len] == source_len


if __name__ == "__main__":
    sl = Solution()
    print sl.isMatch('a','ab*')

