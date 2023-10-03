# every node has 2 distinct counters: prefix and whole word
# only mutated by insert and delete
class TrieNode:
    def __init__(self, c=""):
        self.c = c
        self.children = {}
        self.prefix_cnt = 0
        self.word_cnt = 0
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
            node.prefix_cnt += 1
        node.word_cnt += 1
        
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            else:
                node = node.children[c]
        return node.word_cnt
        
    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            else:
                node = node.children[c]
        return node.prefix_cnt
        
    # It is guaranteed that for any function call to erase,
    # the string word will exist in the trie
    def erase(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            node.prefix_cnt -= 1
        node.word_cnt -= 1

