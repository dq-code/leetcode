class Solution(object):
    def helper(self, nums, n, k):
        if len(nums) == 0: return []
        if len(nums) == 1: return nums

        com_num = 1
        for i in range(1, n):
            com_num = com_num * i
        sub_k = k % com_num
        index = k / com_num
        if sub_k == 0:
            sub_k = com_num
            index -= 1

        com = [nums[index]] + self.helper(nums[:index] + nums[index + 1:], n - 1, sub_k)

        return com

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        if n == 1 and k == 1:
            return '1'

        nums = list(range(1, n + 1))
        permutation = self.helper(nums, n, k)
        return ''.join(str(i) for i in permutation)
