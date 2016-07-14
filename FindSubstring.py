class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []

        word_num = len(words)
        len_of_word = len(words[0])
        total_word_len = word_num * len_of_word
        if len(s) < total_word_len: return []

        res = []
        freq_dict = {}
        for w in words:
            if w not in freq_dict:
                freq_dict[w] = 1
            else:
                freq_dict[w] += 1

        for index in range(len(s) - total_word_len + 1):
            walker = 0
            cur_dict = {}
            while walker < word_num:
                current_word = s[index + walker * len_of_word:index + (walker + 1) * len_of_word]
                if current_word not in freq_dict:
                    break
                else:
                    if current_word not in cur_dict:
                        cur_dict[current_word] = 1
                    else:
                        cur_dict[current_word] += 1
                    if freq_dict[current_word] < cur_dict[current_word]:
                        break
                walker += 1

            if walker == word_num:
                res.append(index)

        return res
