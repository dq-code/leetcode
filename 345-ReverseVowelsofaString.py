class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels='aeiouAEIOU'
        start,end=0,len(s)-1
        res = list(s)
        while start<end:
            while start<len(s) and s[start] not in vowels:
                start += 1
            while end>=0 and s[end] not in vowels:
                end -= 1
            if start>=end: break
            res[start],res[end] = res[end],res[start]
            start += 1
            end -= 1
        return ''.join(res)