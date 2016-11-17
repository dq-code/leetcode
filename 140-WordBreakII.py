class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res = []
        length = len(s)

        def check(s):
            map = [False for x in range(len(s) + 1)]
            map[0] = True
            for i in range(1, len(s) + 1):
                for k in range(0, i):
                    if map[k] and s[k:i] in wordDict:
                        map[i] = True
            return map[len(s)]

        def helper(index, sentence):
            if not check(s[index:]): return
            if index == length:
                res.append(sentence)

            for i in range(index, length):
                word = s[index:i + 1]
                if word in wordDict:
                    newSentence = sentence + " " + word if sentence != "" else word
                    helper(i + 1, newSentence)

        helper(0, "")
        return res
