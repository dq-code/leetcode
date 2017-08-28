class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 1
        nums = [9]
        n = n if n<=10 else 10
        for i in range(9, 9-n+1, -1):
            nums.append(nums[-1]*i)

        return sum(nums)+1