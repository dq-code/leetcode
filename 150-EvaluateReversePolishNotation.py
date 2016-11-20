class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = operand1 + operand2
                stack.append(res)
            elif tokens[i] == '-':
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = operand2 - operand1
                stack.append(res)
            elif tokens[i] == '*':
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = operand1 * operand2
                stack.append(res)
            elif tokens[i] == '/':
                operand1 = stack.pop()
                operand2 = stack.pop()
                if operand1 * operand2 < 0:
                    res = -((-operand2) / operand1)
                else:
                    res = operand2 / operand1
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
