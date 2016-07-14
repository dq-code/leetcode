class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        digits.append(0)

        for i in range(len(digits)-1, 0, -1):
            res = digits[i-1] + carry
            #print i
            #print res
            if res >= 10:
                carry = 1
                digits[i] = res%10
            else:
                carry = 0
                digits[i] = res
        if carry>0:
            digits[0] = 1
            return digits
        return digits[1:] 