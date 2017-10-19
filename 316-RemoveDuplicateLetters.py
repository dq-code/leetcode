import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letter_map = collections.Counter(s)
        stack = []
        for i in range(len(s)):
            letter_map[s[i]] -= 1
            if s[i] in stack:
                continue
            while stack and stack[-1] > s[i] and letter_map[stack[-1]] > 0:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)
