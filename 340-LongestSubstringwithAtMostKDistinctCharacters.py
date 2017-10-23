import collections


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not k: return 0
        dist_map = collections.defaultdict(int)
        max_length = 0
        start = 0
        for i, c in enumerate(s):
            dist_map[c] += 1
            while len(dist_map) > k and start < i:
                dist_map[s[start]] -= 1
                if dist_map[s[start]] == 0:
                    del dist_map[s[start]]
                start += 1
            # print dist_map
            if len(dist_map) == k:
                max_length = max(max_length, sum(dist_map.values()))
        max_length = max(max_length, sum(dist_map.values()))
        return max_length

