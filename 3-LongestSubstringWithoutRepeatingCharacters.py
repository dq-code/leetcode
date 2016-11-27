class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        occurance = {}
        startIndex = 0
        longest = 0
        curLength = 0
        for i in range(len(s)):
            if s[i] not in occurance or occurance[s[i]] < startIndex:
                curLength += 1
                occurance[s[i]] = i
            else:
                if curLength > longest:
                    longest = curLength
                startIndex = occurance[s[i]] + 1
                occurance[s[i]] = i
                curLength = i - startIndex + 1
        if curLength > longest: longest = curLength
        return longest
