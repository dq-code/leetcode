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

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        if self.oneDiff(beginWord,endWord):
            return 2

        self.wordList = list(wordList)
        self.chainMap = {}
        self.buildChainMap()

        queue = [[beginWord,1,[]]]
        while len(queue)>0:
            pair = queue.pop(0)
            word = pair[0]
            length = pair[1]
            path = pair[2]
            for w in self.chainMap[word]:
                if w == endWord:
                    return length+1
                if w not in path:
                    newpath = list(path)
                    newpath.append(word)
                    queue.append([w, length+1, newpath])


        return 0

# if __name__ == "__main__":
#     sol = Solution()
#     print sol.ladderLength("hot", "dog", ["hot","dog","dot"])