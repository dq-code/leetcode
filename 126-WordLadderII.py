class Solution(object):
    def helper(self, word, wordlist, matchlist):
        if self.oneLetterDiff(word, self.endWord):
            # print "word is %s"%word
            # print "this matchlist is %s" % matchlist
            matchlist.append(self.endWord)
            if len(matchlist) < self.shortestPath:
                # print "short path is %d"%self.shortestPath
                # print "now short path is %d" % len(matchlist)
                self.shortestPath = len(matchlist)
                self.res = []
                self.res.append(matchlist)
                # print "res is %s"%self.res
                # print "this now matchlist is %s" % matchlist
            elif len(matchlist) == self.shortestPath:
                # print "elif"
                self.res.append(matchlist)
            return

        if len(matchlist) >= self.shortestPath: return
        for w in wordlist:
            if self.oneLetterDiff(word, w) and len(matchlist) + 1 < self.shortestPath:
                newWordlist = list(wordlist)
                newMatchlist = list(matchlist)
                newWordlist.remove(w)
                newMatchlist.append(w)
                self.helper(w, newWordlist, newMatchlist)

    def oneLetterDiff(self, word1, word2):
        if word1 in self.map:
            if word2 in self.map[word1]: return True
        diff = 0
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                diff += 1
                if diff > 1: return False
        if diff == 1:
            if word1 in self.map:
                self.map[word1].add(word2)
            else:
                self.map[word1] = set(word2)

            if word2 in self.map:
                self.map[word2].add(word1)
            else:
                self.map[word2] = set(word1)

        return False

    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if beginWord == endWord:
            return []

        if self.oneLetterDiff(beginWord, endWord):
            print "begin == end"
            return [[beginWord, endWord]]

        self.res = []
        self.shortestPath = len(wordlist)
        self.endWord = endWord
        self.map = {}

        self.helper(beginWord, wordlist, [beginWord])

        return self.res

# if __name__ == "__main__":
#    sol = Solution()
#    print sol.findLadders("hot", "dog", ["hot","dog","dot"])
