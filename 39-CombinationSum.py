class Solution(object):
    def helper(self, candidates, target, combination):
        if sum(combination) == target and combination not in Solution.set:
            Solution.set.append(combination)
            return
        for i in range(len(candidates)):
            if candidates[i] <= target - sum(combination):
                self.helper(candidates[i:], target, combination + [candidates[i]])
            else:
                return

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.set = []
        res = self.helper(candidates, target, [])
        return Solution.set
