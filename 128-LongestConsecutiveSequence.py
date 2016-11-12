class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {x: False for x in nums}
        maxLen = 1
        for key in dict:
            if dict[key] is False:
                dict[key] = True
                cur = key - 1
                length = 1
                while cur in dict and not dict[cur]:
                    length += 1
                    dict[cur] = True
                    cur -= 1
                cur = key + 1
                while cur in dict and not dict[cur]:
                    length+=1
                    dict[cur] = True
                    cur += 1
                maxLen = max(length, maxLen)
        return maxLen