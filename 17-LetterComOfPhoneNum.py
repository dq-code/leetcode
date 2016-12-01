class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        letter_map={"2":"a,b,c", "3":"d,e,f", "4":"g,h,i", "5":"j,k,l", "6":"m,n,o", "7":"p,q,r,s", "8":"t,u,v", "9":"w,x,y,z"}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return letter_map[digits].split(",")
        res = []
        sub_res = self.letterCombinations(digits[1:])
        for letter in letter_map[digits[0]].split(","):
            for combination in sub_res:
                res.append(letter+combination)
        return res

