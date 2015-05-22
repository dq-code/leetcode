class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        map={}
        if s == "":
            return 0
        maxLen = length = 0
        start = 0
        for i in range(len(s)):
            index = map.get(s[i],-1)
            if index < 0 or index < start:
                map[s[i]]=i
                length=length+1
            else:
                if length > maxLen:
                    maxLen = length
                length = i-index
                map[s[i]]=i
                start = index+1
        if length > maxLen:
            maxLen = length
        return maxLen