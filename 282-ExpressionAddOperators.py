class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        post_stack = []
        oper_stack = []
        oper_priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        number = ''
        for c in s:
            if c == ' ': continue
            if c in '0123456789':
                number += c
            else:
                if number:
                    post_stack.append(number)
                    number = ''
                if c == '(': oper_stack.append(c)
                if c in '-+*/':
                    while oper_stack:
                        if oper_stack[-1] != '(' and oper_priority[oper_stack[-1]] >= oper_priority[c]:
                            post_stack.append(oper_stack.pop())
                        else:
                            break
                    oper_stack.append(c)
                if c == ')':
                    while oper_stack[-1] != '(':
                        post_stack.append(oper_stack.pop())
                    oper_stack.pop()
        if number: post_stack.append(number)
        while oper_stack:
            post_stack.append(oper_stack.pop())

        # print post_stack

        val_stack = []
        for i in range(len(post_stack)):
            if post_stack[i] not in '+-*/':
                val_stack.append(post_stack[i])
            else:
                num1 = val_stack.pop()
                num2 = val_stack.pop()

                # print "oper %s, num1 %s and num2 %s"%(post_stack[i], num1, num2)

                if post_stack[i] == '+':
                    value = str(int(num1) + int(num2))
                if post_stack[i] == '-':
                    value = str(int(num2) - int(num1))
                if post_stack[i] == '*':
                    value = str(int(num1) * int(num2))
                if post_stack[i] == '/':
                    value = str(float(num2) / int(num1))
                val_stack.append(value)
        return int(val_stack[0])



