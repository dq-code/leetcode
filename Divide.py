class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return MAX_INT
        if dividend == 0:
            return 0
        minus = False
        if dividend<0 or divisor<0:
           minus = True

        a = abs(dividend)
        b = abs(divisor)

        res = 0
        while b <= a:
            sum = b
            count = 1
            while sum+sum<a:
                sum += sum
                count += count
            a -= sum
            res += count

        if minus:
            return 0-res
        return res