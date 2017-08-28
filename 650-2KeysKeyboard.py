class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        # def helper(curNum, copyNum, step):
        #     if curNum == n:
        #         return step
        #     elif curNum > n:
        #         return n
        #     step += 1
        #     # ACTION PASTE
        #     ncurNum = curNum + copyNum
        #     # print ncurNum
        #     # ACTION COPY IF CURRENT NUMBER CHANGED
        #     if copyNum < curNum:
        #         ncopyNum = curNum
        #         return min(helper(ncurNum, copyNum, step), helper(curNum, ncopyNum, step))
        #     else:
        #         return helper(ncurNum, copyNum, step)
        #
        # if n == 1: return 0
        # return helper(1, 1, 1)


        dp = [n for i in range(n+1)]
        dp[0] = dp[1] = 0
        for i in range(2, n+1):
            for j in range(1, i):
                if i%j == 0:
                    dp[i] = min(dp[i], dp[j]+i/j)
        return dp[-1]