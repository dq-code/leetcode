class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if not rows or not cols: return 0
        if not sentence: return 0

        nword = len(sentence)
        words = [len(sentence[i]) for i in range(nword)]
        counts = [0 for i in range(nword)]
        for i in range(nword):
            c = 0
            wlen = 0
            while wlen + words[(i + c) % nword] <= cols:
                wlen += words[(i + c) % nword] + 1
                c += 1

            counts[i] = c
        # print counts
        wcount = 0
        for j in range(rows):
            wcount += counts[wcount % nword]
        return wcount / nword

