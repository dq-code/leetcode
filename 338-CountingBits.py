class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for x in range(num+1)]
        for i in range(1, len(num+1)):
            res[i] = res[i - (1<<int(math.log(x,2)))] + 1
        return res