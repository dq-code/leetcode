class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for n in nums:
            if n in map:
                del map[n]
            else:
                map[n] = 1

        return map.keys()[0]
