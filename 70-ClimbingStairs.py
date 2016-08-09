class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0: return 0
        cur_step = 0
        step_list = [ 1 for x in range(n)]
        for i in range(1, n):
            step_list[i] = step_list[i-1]+step_list[i-2]
        return step_list[n-1]



