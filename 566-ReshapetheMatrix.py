class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        res = []
        cloop = 0
        rloop = 0
        tmplist = []
        for list in nums:
            for item in list:
                tmplist.append(item)
                cloop += 1
                if cloop == c:
                    cloop = 0
                    res.append(tmplist)
                    tmplist = []
                    rloop += 1
        return res
