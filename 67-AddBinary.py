class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        walkerA = len(a) - 1
        walkerB = len(b) - 1

        carry = 0
        sum = ''
        while walkerA >= 0 and walkerB >= 0:
            if a[walkerA] == '1' and b[walkerB] == '1':
                res = carry
                carry = 1
            elif a[walkerA] == '1' or b[walkerB] == '1':
                if carry == 0:
                    res = 1
                    carry = 0
                else:
                    res = 0
                    carry = 1
            elif a[walkerA] == '0' and b[walkerB] == '0':
                res = carry
                carry = 0
            sum = str(res) + sum
            walkerA -= 1
            walkerB -= 1

        # print 'walkerA is %d and walkerB is %d'%(walkerA, walkerB)
        while walkerA >= 0:
            if a[walkerA] == '1':
                if carry == 1:
                    res = 0
                    carry = 1
                else:
                    res = 1
                    carry = 0
            else:
                res = carry
                carry = 0
            sum = str(res) + sum
            walkerA -= 1

        while walkerB >= 0:
            if b[walkerB] == '1':
                if carry == 1:
                    res = 0
                    carry = 1
                else:
                    res = 1
                    carry = 0
            else:
                res = carry
                carry = 0
            sum = str(res) + sum
            walkerB -= 1

        if carry == 1:
            sum = '1' + sum

        return sum
