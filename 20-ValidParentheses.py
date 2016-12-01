class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        p_map = {")":"(", "}":"{", "]":"["}
        store_ls = []
        for i in range(len(s)):
            if not p_map.has_key(s[i]):
                store_ls.append(s[i])
            else:
                if len(store_ls) == 0:
                    return False
                else:
                    if store_ls.pop() != p_map[s[i]]: return False
        if len(store_ls)==0: return True
        return False

