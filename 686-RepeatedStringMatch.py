class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        x = int(math.ceil(float(len(B)) / len(A)))
        if B in A * x:
            return x
        if B in A * (x + 1):
            return x + 1

        return -1 