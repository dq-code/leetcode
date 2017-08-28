class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = None, 0
        for item in nums:
            if count == 0:
                candidate, count = item, 1
            elif candidate==item:
                count += 1
            else:
                count -= 1

        return candidate

