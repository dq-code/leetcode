class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def helper(comb, start, k):
            if k == 0:
                res.append(comb)
                return
            for i in range(start, n + 1):
                if n - start + 1 >= k:
                    helper(comb + [i], i + 1, k - 1)

        res = []
        helper([], 1, k)
        return res
