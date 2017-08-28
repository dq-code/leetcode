class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_ls = str.split(' ')
        if len(pattern) != len(str_ls): return False
        match = {}
        index = 0
        while index < len(pattern):
            if pattern[index] in match:
                if match[pattern[index]] != str_ls[index]:
                    return False
            else:
                if str_ls[index] in match.values():
                    return False
                match[pattern[index]] = str_ls[index]
            index += 1
        return True

