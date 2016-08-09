class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathl = len(path)

        stack = []
        walker = 0
        while walker < pathl:
            i = walker + 1
            while i < pathl:
                if path[i] == '/':
                    break
                i = i + 1
            if i > walker + 1:
                dirName = path[walker + 1:i]
                if dirName == '..':
                    if len(stack) > 0:
                        stack.pop()
                elif dirName != '.':
                    stack.append('/' + dirName)
            walker = i

        res = ''
        if len(stack) == 0:
            return '/'
        else:
            for subpath in stack:
                res += subpath

        return res
