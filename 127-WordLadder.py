class Solution(object):
    def oneDiff(self, word1, word2):
        if word1==word2:
            return False

        diff = 0
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                diff += 1
                if diff > 1: return False

        return True

    def buildChainMap(self):
        for i in range(0, len(self.wordList)-1):
            for j in range(i+1, len(self.wordList)):
                if self.oneDiff(self.wordList[i], self.wordList[j]):
                    if self.wordList[i] not in self.chainMap:
                        self.chainMap[self.wordList[i]] = [self.wordList[j]]
                    else:
                        self.chainMap[self.wordList[i]].append(self.wordList[j])
                    if self.wordList[j] not in self.chainMap:
                        self.chainMap[self.wordList[j]] = [self.wordList[i]]
                    else:
                        self.chainMap[self.wordList[j]].append(self.wordList[i])

    def helper(self, word, visited, pathLen):
        if word not in self.chainMap:
            return
        if self.endWord in self.chainMap[word]:
            if pathLen+1 < self.shortestPath:
                self.shortestPath = pathLen + 1
            return

        for w in self.chainMap[word]:
            if w not in visited:
                newVisited = list(visited)
                newVisited.append(word)
                self.helper(w, newVisited, pathLen+1)

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        if self.oneDiff(beginWord,endWord):
            return 2

        self.endWord = endWord
        self.wordList = wordList
        self.chainMap = {}
        self.shortestPath = len(wordList)+100

        self.buildChainMap()
        self.helper(beginWord, [], 1)

        if self.shortestPath == len(wordList)+100: return 0
        return self.shortestPath

# if __name__ == "__main__":
#     sol = Solution()
#     print sol.ladderLength("hot", "dog", ["hot","dog","dot"])