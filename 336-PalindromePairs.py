class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def isSelfPanlindrom(word):
            start = 0
            end = len(word) - 1
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True

        word_map = {y: x for x, y in enumerate(words)}
        res = set()
        for index, word in enumerate(words):
            if "" in word_map and word != "" and isSelfPanlindrom(word):
                res.add((word_map[""], index))
                res.add((index, word_map[""]))

            reversed_word = word[::-1]
            if reversed_word in word_map and word_map[reversed_word] != index:
                res.add((word_map[reversed_word], index))

            for i in range(1, len(word)):
                right = word[0:i]
                left = word[i:]
                reversed_left = left[::-1]
                reversed_right = right[::-1]
                if isSelfPanlindrom(right) and reversed_left in word_map:
                    res.add((word_map[reversed_left], index))
                if isSelfPanlindrom(left) and reversed_right in word_map:
                    res.add((index, word_map[reversed_right]))

        return list(res)
