class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strobogrammatic_map = {'6': '9', '9': '6', '0': '0', '1': '1', '8': '8'}
        new_num = ''
        for c in num:
            if c in strobogrammatic_map:
                new_num = strobogrammatic_map[c] + new_num
            else:
                return False

        return new_num == num