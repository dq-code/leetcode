class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        max_len = 0
        for p in input.split('\n'):
            cur_depth = p.count('\t')
            while stack and cur_depth < len(stack):
                if '.' in stack[-1]:
                    max_len = max(max_len, len(''.join(stack)))
                stack.pop()
            new_file = p.lstrip('\t')
            if not '.' in new_file:
                new_file += '/'
            stack.append(new_file)
        if '.' in stack[-1]:
            max_len = max(max_len, len(''.join(stack)))
        return max_len


