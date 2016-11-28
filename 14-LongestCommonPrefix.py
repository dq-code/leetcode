class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        common_prefix = ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        minLengh = 99999
        shortest_index = -1
        for i in range(len(strs)):
            if len(strs[i]) < minLengh:
                minLengh = len(strs[i])
                shortest_index = i
        common_index_ls = [0 for x in range(len(strs[shortest_index]))]
        for i in range(len(common_index_ls)):
            for j in range(len(strs)):
                if strs[shortest_index][i] == strs[j][i]:
                    common_index_ls[i] += 1
        
        for i in range(len(common_index_ls)):
            if common_index_ls[i] == len(strs):
                common_prefix += strs[shortest_index][i]
            else: break

        return common_prefix