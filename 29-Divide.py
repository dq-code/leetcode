class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0: return MAX_INT
        if dividend == 0: return 0
        sign = 1
        if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0): sign = -1
        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            sum = divisor
            count = 1
            while sum + sum < dividend:
                sum += sum
                count += count
            dividend -= sum
            res += count
        if sign < 0:
            return 0 - res
        if res >= 2147483647: res = 2147483647
        return res
