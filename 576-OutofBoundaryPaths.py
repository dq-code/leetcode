class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        dp = [[0 for x in range(n)] for y in range(m)]
        dp[i][j] = 1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        res = 0
        mod = 1000000007
        for cnt in range(N):
            ndp = [[0 for x in range(n)] for y in range(m)]
            for l in range(m):
                for k in range(n):
                    for dir in dirs:
                        nrow = l+dir[0]
                        ncol = k + dir[1]
                        #print "row %d, col %d, nrow %d, ncol %d"%(l,k,nrow,ncol)
                        if nrow < 0 or nrow >= m or ncol < 0 or ncol >= n:
                            res = (res + dp[l][k])%mod
                        else:
                            ndp[nrow][ncol] = (ndp[nrow][ncol]+dp[l][k])%mod
            dp = ndp
        return res