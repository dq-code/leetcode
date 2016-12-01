class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n==0:
            return []
        res = []
        sub_res = self.generateParenthesis(n-1)
        if len(sub_res) == 0:
            return ["()"]
        for pattern in sub_res:
            for i in range(len(pattern)):
                newp = pattern[0:i+1]+"()"+pattern[i+1:]
                if sub_res.count(newp) == 0:
                    sub_res.append(newp)
        return res


