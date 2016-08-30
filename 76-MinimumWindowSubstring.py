class Solution(object):
    def push(self, element):
        if element in self.refMap.keys():
            if element in self.numMap.keys():
                self.numMap[element] += 1
                if self.posMap[element] < self.refMap[element]:
                    self.posMap[element] += 1
            else:
                self.numMap[element] = 1
                self.posMap[element] = 1

    def pop(self, element):
        if element in self.numMap.keys():
            self.numMap[element] -= 1
            if self.numMap[element] < self.refMap[element]:
                self.posMap[element] -= 1
            return True
        else:
            return False

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = sorted(t)
        self.refMap = {}
        for i in range(len(t)):
            if t[i] in self.refMap:
                self.refMap[t[i]] += 1
            else:
                self.refMap[t[i]] = 1
        # print self.refMap
        self.numMap = {}
        self.posMap = {}
        head = tail = 0
        minWin = len(s) + 1
        minStart = minEnd = -1
        while tail < len(s):
            self.push(s[tail])
            if sum(self.posMap.values()) == sum(self.refMap.values()):
                while head <= tail:
                    if self.pop(s[head]):
                        curWin = tail - head + 1
                        # print 'curWin is %d, head is %d, tail is %d' % (curWin, head, tail)
                        if curWin < minWin:
                            minStart = head
                            minEnd = tail
                            minWin = curWin
                        if sum(self.posMap.values()) < sum(self.refMap.values()):
                            head += 1
                            break
                    head += 1
            # print tail
            tail += 1

        if minStart == -1:
            return ''
        return s[minStart:minEnd + 1]
