class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total = 0
        for i in range(len(num1)):
            m1 = int(num1[i])
            carry = [0 for x in range(len(num2) + 1)]
            for j in range(len(num2) - 1, -1, -1):
                m2 = int(num2[j])
                result = m1 * m2
                carry[j + 1] = result % 10 + carry[j + 1]
                carry[j] = result / 10
            subsum = 0
            for t in range(len(carry)):
                subsum = subsum * 10 + carry[t]
            total = total * 10 + subsum

        total_str = ''
        while total / 10 > 0:
            char = total / 10
            total = total % 10
            total_str += str(char)

        total_str += str(total)

        return total_str
