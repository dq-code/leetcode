class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand = []
        priority = {'+': 0, '-': 0, '*': 1, '/': 1}
        num = ''
        for c in s:
            if c == ' ':
                continue
            elif c in '0123456789':
                num = num + c
            else:
                if num:
                    stack.append(int(num))
                    num = ''
                while operand and priority[operand[-1]] >= priority[c]:
                    stack.append(operand.pop())
                operand.append(c)
        if num:
            stack.append(int(num))
        while operand:
            stack.append(operand.pop())
        operands = []
        for c in stack:
            if c == '+':
                y = operands.pop()
                x = operands.pop()
                operands.append(x + y)
            elif c == '*':
                y = operands.pop()
                x = operands.pop()
                operands.append(x * y)
            elif c == '-':
                y = operands.pop()
                x = operands.pop()
                operands.append(x - y)
            elif c == '/':
                y = operands.pop()
                x = operands.pop()
                operands.append(x / y)
            else:
                operands.append(c)
        return operands[0]









