class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dict:
                dict[key] = [word]
            else:
                dict[key] += [word]

        res = []
        for val in dict.values():
            res.append(val)

        return res
