class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        res = 0
        prevDiff = A[1]-A[0]
        curDiffNum = 1
        i = 2
        while i < len(A):
            curDiff = A[i]-A[i-1]
            if curDiff == prevDiff:
                curDiffNum += 1
            else:
                prevDiff = curDiff
                res += sum([x for x in range(1, curDiffNum)])
                curDiffNum = 1
            i += 1
        res += sum([x for x in range(1, curDiffNum)])
        return res