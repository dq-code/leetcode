import collections


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        records = collections.defaultdict(list)
        start = 0
        max_len = 0
        for i in range(len(s)):
            records[s[i]].append(i)

            if len(records) <= 2:
                max_len = max(max_len, i - start + 1)
            else:
                while len(records) > 2:
                    records[s[start]].pop(0)
                    if len(records[s[start]]) == 0:
                        del records[s[start]]
                    start += 1
        return max_len