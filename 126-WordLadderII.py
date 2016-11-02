class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        res = []
        prevMap = {}

        for w in wordlist:
            prevMap[w] = []
        candidates = [set(), set()]
        current = 0
        previous = 1
        candidates[current].add(beginWord)

        def buildpath(path, word):
            if len(prevMap[word]) == 0:
                path.append(word);
                currPath = path[:]
                currPath.reverse();
                res.append(currPath)
                path.pop();
                return
            path.append(word)
            for iter in prevMap[word]:
                buildpath(path, iter)
            path.pop()

        while True:
            current, previous = previous, current
            for w in candidates[previous]:
                wordlist.remove(w)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(len(word)):
                    front = word[:i]
                    back = word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            tempWord = front + j + back
                            if tempWord in wordlist:
                                prevMap[tempWord].append(word)
                                candidates[current].add(tempWord)
            if len(candidates[current]) == 0: return res
            if endWord in candidates[current]: break

        buildpath([], endWord)

        return res

        # if __name__ == "__main__":
        #     sol = Solution()
        #     print sol.ladderLength("hot", "dog", ["hot","dog","dot"])
