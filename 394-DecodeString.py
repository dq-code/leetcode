class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''

        index = 0
        res = ''

        digit_stack = []
        str_stack = []
        while index < len(s):
            if s[index].isdigit():
                num = ''
                while s[index].isdigit():
                    num += s[index]
                    index += 1
                digit_stack.append(int(num))
            elif s[index] == '[':
                index += 1
                part = ''
                while index < len(s):
                    if s[index].isdigit() or s[index] in '[]':
                        break
                    part += s[index]
                    index += 1
                str_stack.append(part)
            elif s[index] == ']':
                part = str_stack.pop() * digit_stack.pop()
                if str_stack:
                    str_stack[-1] += part
                else:
                    res += part
                index += 1
            else:
                if not str_stack:
                    res += s[index]
                else:
                    str_stack[-1] += s[index]
                index += 1
                # print digit_stack
                # print str_stack

        return res
