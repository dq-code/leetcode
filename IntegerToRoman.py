class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        c_dir = {1000:"M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}
        roman = ""
        k_ls = [1000, 500, 100, 50, 10, 5, 1]
        index = 0
        residue = num
        while residue > 0:
            print "!!index is %s for %i"%(k_ls[index],residue)
            print "times %i"% (residue/k_ls[index])
            roman = roman + c_dir[k_ls[index]]*(residue/k_ls[index])
            residue = residue%k_ls[index]
            print "mod is %s"%residue
            if k_ls[index]>100: unit = 100
            elif k_ls[index] > 10: unit = 10
            elif k_ls[index] > 1: unit = 1
            else: unit = 0
            if k_ls[index]-residue <= unit:
                print "unit is %s"%unit
                roman = roman + c_dir[unit]+c_dir[k_ls[index]]
                residue = residue - (k_ls[index]-unit)
                print "residue is %s"%residue
            index = index + 1
            print roman
        return roman

if __name__ == "__main__":
    input = 91
    runner = Solution()
    print runner.intToRoman(input)



