import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) > len(nums1): return self.intersect(nums2, nums1)

        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)

        res = []
        for key,value in c2.iteritems():
            if key in c1:
                minC = min(value, c1[key])
                res += [key]*minC

        return res