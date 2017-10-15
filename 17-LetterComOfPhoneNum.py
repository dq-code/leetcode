class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                   "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}

        def helper(pos):
            if pos >= len(digits): return ['']
            combs = helper(pos + 1)
            res = []
            for char in mapping[digits[pos]]:
                for ss in combs:
                    res.append(char + ss)
            return res

        if not digits: return []
        return helper(0)
