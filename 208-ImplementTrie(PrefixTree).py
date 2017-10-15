class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        # print self.root.children
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        index = 0
        node = self.root
        while index < len(word):
            if not word[index] in node.children:
                # print "search not find key "
                # print node.children
                return False
            node = node.children[word[index]]
            index += 1
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        index = 0
        node = self.root
        while index < len(prefix):
            if not prefix[index] in node.children:
                return False
            node = node.children[prefix[index]]
            index += 1
        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)