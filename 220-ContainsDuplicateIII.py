import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums: return False
        if t < 0: return False
        look_up = collections.OrderedDict()
        for i in range(len(nums)):
            key = nums[i] / (t + 1)
            if any([v in look_up and abs(look_up[v] - nums[i]) <= t for v in [key - 1, key, key + 1]]): return True
            look_up[key] = nums[i]
            if i >= k:
                look_up.popitem(last=False)
        return False
