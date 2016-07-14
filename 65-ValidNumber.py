class Solution(object):
    def allDigit(self, subS, allowEmpty, allowE, allowFirstE, allowPlus):
        # print allowEmpty
        # print allowE

        if not allowEmpty and len(subS) == 0: return False
        if len(subS) == 1 and subS[0] not in '0123456789': return False

        hasE = False
        for i in range(len(subS)):
            if i == 0 and not allowFirstE and subS[i] in 'eE': return False
            if i == 0 and allowPlus and subS[i] in '+-': continue
            if allowE and not hasE:
                if subS[i] not in 'Ee0123456789':
                    return False
                elif subS[i] in 'Ee':
                    if i == len(subS) - 1: return False
                    hasE = True
                    continue
            if allowE and hasE:
                if subS[i] in '-+':
                    if subS[i - 1] == 'e':
                        continue
                    else:
                        return False
            if subS[i] not in '0123456789': return False
        return True

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        length = len(s)
        if length == 0: return False

        hasFlag = False

        if length == 1 and s[0] not in '0123456789': return False
        if s[0] not in '-+0123456789.':
            return False
        elif s[0] == '.':
            return self.allDigit(s[1:], False, True, False, False)
        elif s[0] in '-+':
            hasFlag = True

        for i in range(1, length):
            # print s[i]
            if i == 1 and hasFlag and s[i] == '.': return self.allDigit(s[i + 1:], False, True, True, False)
            if i == 1 and hasFlag and s[i] in 'eE': return False
            if s[i] not in '0123456789.eE':
                # print 'not valid element'
                return False
            elif s[i] == '.' or s[i] in 'eE':
                # print s[i]
                return self.allDigit(s[i + 1:], s[i] == '.', s[i] not in 'eE', s[i] not in 'eE', s[i] in 'eE')

        return True
