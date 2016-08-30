class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        l1 = len(s1)
        l2 = len(s2)

        if l1 + l2 != len(s3): return False

        dp = [[0 for i in range(l1 + 1)] for j in range(l2 + 1)]
        dp[0][0] = 1

        index = 0
        while index < l1:
            if s1[index] == s3[index]:
                dp[0][index + 1] = 1
                index += 1
            else:
                break

        index = 0
        while index < l2:
            if s2[index] == s3[index]:
                dp[index + 1][0] = 1
                index += 1
            else:
                break

        # print dp
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if dp[i - 1][j] == 1:
                    # print "i-1 is %d and j is %d"%((i-1),j)
                    if s2[i - 1] == s3[i + j - 1]:
                        dp[i][j] = 1
                        # print dp
                if dp[i][j - 1] == 1:
                    # print "i is %d and j-1 is %d"%(i,j-1)
                    if s1[j - 1] == s3[i + j - 1]:
                        dp[i][j] = 1

        return dp[l2][l1] == 1
