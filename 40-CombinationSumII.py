class Solution(object):
    def helper(self, candidates, target, combination):
        if sum(combination) == target:
            if combination not in Solution.set:
                Solution.set.append(combination)
                return

        for i in range(len(candidates)):
            total = sum(combination) + candidates[i]
            if total <= target:
                self.helper(candidates[i + 1:], target, combination + [candidates[i]])
            else:
                return

        return

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.set = []
        candidates.sort()
        self.helper(candidates, target, [])
        return Solution.set
