class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = [n]
        walker = n
        while True:
            res = 0
            while walker > 0:
                res += (walker%10)**2
                walker = walker/10
            walker = res
            if walker == 1:
                return True
            if walker in nums:
                return False
            nums.append(walker)

        return False