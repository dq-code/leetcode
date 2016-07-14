class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        ele_dict = {}
        previous_dup_list = [-1] * len(needle)
        for i in range(len(needle)):
            if not needle[i] in ele_dict:
                ele_dict[needle[i]] = i
            else:
                previous_dup_list[i] = ele_dict.get(needle[i])
                ele_dict[needle[i]] = i

        index = len(needle) - 1
        while index < len(haystack):
            walker_index = 0
            while walker_index < len(needle):
                if haystack[index - walker_index] != needle[len(needle) - walker_index - 1]:
                    break
                walker_index = walker_index + 1
            if walker_index == len(needle): return index - len(needle) + 1
            if walker_index > 0:
                if previous_dup_list[len(needle) - walker_index] != -1:
                    index = index - (walker_index - 1) + len(needle) - (
                    previous_dup_list[len(needle) - walker_index] + 1)
                else:
                    index = index - (walker_index - 1) + len(needle)
            else:
                index = index + 1

        return -1
