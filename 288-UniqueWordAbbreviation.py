import collections


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbt_map = collections.defaultdict(set)
        for w in dictionary:
            self.abbt_map[self.getAbbr(w)].add(w)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.getAbbr(word)
        return abbr not in self.abbt_map or (len(self.abbt_map[abbr]) == 1 and list(self.abbt_map[abbr])[0] == word)

    def getAbbr(self, word):
        if len(word) <= 2: return word
        return word[0] + str(len(word) - 2) + word[-1]



        # Your ValidWordAbbr object will be instantiated and called as such:
        # obj = ValidWordAbbr(dictionary)
        # param_1 = obj.isUnique(word)