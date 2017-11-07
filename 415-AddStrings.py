class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        i = 0
        res = ''
        residue = 0
        while i < len(num1) and i < len(num2):
            cur = int(num1[i]) + int(num2[i]) + residue
            res = str(cur % 10) + res
            residue = cur / 10
            i += 1
        if i < len(num1):
            while i < len(num1):
                cur = int(num1[i]) + residue
                res = str(cur % 10) + res
                residue = cur / 10
                i += 1
        if i < len(num2):
            while i < len(num2):
                cur = int(num2[i]) + residue
                res = str(cur % 10) + res
                residue = cur / 10
                i += 1
        return '1' + res if residue else res

