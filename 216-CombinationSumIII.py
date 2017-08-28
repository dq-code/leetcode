class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(comb,start):
            if len(comb)==k:
                #print comb
                if sum(comb)==n:
                    res.append(comb)
                return
            for i in range(start,10):
                if i not in comb and sum(comb)+i<=n:
                    helper(comb+[i], i+1)

        helper([],1)

        return res
