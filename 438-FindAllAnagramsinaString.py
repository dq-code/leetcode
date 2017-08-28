import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counterP = collections.Counter(p)
        counter0 = {char:0 for char in p}
        nums = len(p)
        index = 0
        res = []
        while index<len(s):
            #print counterP
            if s[index] not in counterP:
                counterP = collections.Counter(p)
                nums = len(p)
            else:
                counterP[s[index]] -= 1
                nums -= 1
                if nums == 0:
                    #print "num 0, index %d"%index
                    #print counterP
                    if counterP==counter0:
                        res.append(index-len(p)+1)
                    nums += 1
                    counterP[s[index-len(p)+1]] += 1
            index += 1
        return res

