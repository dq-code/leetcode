class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        queue = [[beginWord, 1]]

        while len(queue) > 0:
            comb = queue.pop(0)
            word = comb[0]
            length = comb[1]
            for i in range(len(word)):
                front = word[:i]
                back = word[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] != j:
                        tempWord = front + j + back
                        if tempWord == endWord:
                            return length + 1
                        if tempWord in wordList:
                            wordList.remove(tempWord)
                            queue.append([tempWord, length + 1])

        return 0

        # if __name__ == "__main__":
        #     sol = Solution()
        #     print sol.ladderLength("hot", "dog", ["hot","dog","dot"])
