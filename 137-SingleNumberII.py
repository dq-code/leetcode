class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for n in nums:
            if n in map:
                if map[n] == 2:
                     del map[n]
                else:
                    map[n] += 1
            else:
                map[n] = 1

        return map.keys()[0]