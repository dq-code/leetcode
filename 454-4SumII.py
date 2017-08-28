import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        sumMap1 = collections.defaultdict(int)
        for i in A:
            for j in B:
                sumMap1[i+j] += 1

        res = 0
        for i in C:
            for j in D:
                res += sumMap1[-(i+j)]

        return res
