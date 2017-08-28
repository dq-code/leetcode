class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def toString(self):
        if self.start==self.end:
            return str(self.start)
        return str(self.start)+"->"+str(self.end)

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0: return []

        res = [Range(nums[0],nums[0])]


        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                #print "continue %d"%i
                res[-1].end = nums[i]
            else:
                #print "new start %d"%i
                res.append(Range(nums[i], nums[i]))

        for i in range(len(res)):
            res[i] = res[i].toString()

        return res


