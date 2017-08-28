import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        q = [1]
        q2 = 0
        q3 = 0
        q5 = 0
        curPos = 1
        while len(q)<n:
            value2 = 2*q[q2]
            value3 = 3*q[q3]
            value5 = 5*q[q5]
            minV = min(value2, value3, value5)
            if minV==value2:
                q2 += 1
            if minV==value3:
                q3 += 1
            if minV==value5:
                q5 += 1
            q.append(minV)
        return q[-1]



