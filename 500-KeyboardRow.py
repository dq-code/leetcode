class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        sets = map(set, ['qwertyuiop','asdfghjkl','zxcvbnm'])

        res = []
        for word in words:
            wordL = set(word.lower())
            if any(set(word) <= ss for ss in sets):
                res.append(word)

        return res