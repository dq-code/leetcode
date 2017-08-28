class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        localMin = arrays[0][0]
        localMax = arrays[0][-1]

        res = 0

        for i in range(1, len(arrays)):
            res = max(res, abs(arrays[i][-1]-localMin),abs(localMax-arrays[i][0]))
            localMin = min(localMin, arrays[i][0])
            localMax = max(localMax, arrays[i][-1])
            
        return res