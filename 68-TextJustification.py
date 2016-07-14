class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth == 0:
            return [""]
        length = len(words)
        i = 0
        res = []
        buffer = ''
        while i < length:
            if buffer == '' and len(words[i]) <= maxWidth:
                buffer = words[i]
            elif len(buffer) > 0 and len(buffer) + len(words[i]) + 1 <= maxWidth:
                buffer = buffer + ' ' + words[i]
            else:
                temp_list = buffer.split()
                buffer = words[i]
                temp_list_len = len(temp_list)
                words_len = sum(len(temp_list[j]) for j in range(temp_list_len))
                space_num = maxWidth - words_len
                divide = temp_list_len - 1 if temp_list_len > 1 else 1
                space_list = ['' for j in range(divide)]
                # print temp_list
                while divide > 0 and space_num > 0:
                    # print 'divide is %d and space_num is %d' % (divide, space_num)
                    space = space_num / divide
                    # print 'space is %d'%space
                    space_num = space_num % divide
                    for j in range(0, divide):
                        space_list[j] += ' ' * space
                    divide -= 1
                temp = ''
                if temp_list_len == 1:
                    temp = temp_list[0] + space_list[0]
                else:
                    for j in range(0, temp_list_len - 1):
                        temp += temp_list[j] + space_list[j]
                    temp += temp_list[temp_list_len - 1]
                res.append(temp)
            i += 1

        temp_list = buffer.split()
        if len(temp_list) == 0:
            if len(res) == 0 and maxWidth > 0:
                res.append(' ' * maxWidth)
            return res

        temp_str = temp_list[0]
        for j in range(1, len(temp_list)):
            temp_str += ' ' + temp_list[j]
        temp_len = len(temp_str)
        left_len = maxWidth - temp_len
        temp_str += ' ' * left_len
        res.append(temp_str)

        return res
