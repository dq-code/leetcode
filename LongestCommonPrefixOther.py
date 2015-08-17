class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        common_prefix = "0"
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix_dir = {}
        for i in range(1, len(strs)):
            j = 0
            prefix = "0"
            while j in range(len(strs[0])) and j in range(len(strs[i])) and strs[0][j] == strs[i][j]:
                prefix += strs[0][j]
                j = j + 1
            if len(prefix) > len(common_prefix):
                common_prefix = prefix
            if not prefix_dir.has_key(prefix):
                prefix_dir[prefix]=[]
            prefix_dir[prefix].append(j)
        for key in prefix_dir.keys():
            if len(prefix_dir[key]) > 1:
                list = []
                for index in prefix_dir[key]:
                    list.append(strs[index][len(key):])
                prefix = key+longestCommonPrefix(list)
                if len(prefix) > len(common_prefix):
                    common_prefix = prefix

        return common_prefix



