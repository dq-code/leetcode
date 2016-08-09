class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0: return 0

        high_end = x/2 + 1
        low_end = 1
        while high_end >= low_end:
            mid = (high_end - low_end)/2 + low_end
            sq_mid = mid * mid
            if sq_mid == x:
                return mid
            elif sq_mid < x:
                low_end = mid+1
            else:
                high_end = mid-1

        return high_end
