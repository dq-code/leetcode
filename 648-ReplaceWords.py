class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def _chartoIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        node = self.root
        index = 0
        while index < len(word):
            key = self._chartoIndex(word[index])
            if node.children[key] is None:
                node.children[key] = TrieNode()
            node = node.children[key]
            index += 1
        node.isWord = True

    def search(self, word):
        node = self.root
        res = ''
        index = 0
        while index < len(word):
            key = self._chartoIndex(word[index])
            node = node.children[key]
            if node is None:
                break
            res += word[index]
            if node.isWord:
                return res
            index += 1

        return word


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for w in dict: trie.insert(w)

        res = []
        for w in sentence.split(' '):
            res.append(trie.search(w))

        return ' '.join(res)