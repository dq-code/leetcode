class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_len = 0
        stack = []
        last = -1

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        longest_len = max(longest_len, i - last)
                    else:
                        longest_len = max(longest_len, i - stack[-1])

        return longest_len
