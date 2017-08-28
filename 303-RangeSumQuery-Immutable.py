class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.curSum = [0 for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            self.curSum[i] = self.curSum[i - 1] + nums[i - 1]
        print self.curSum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.curSum[j + 1] - self.curSum[i]



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)