class TrieNode:
    def __init__(self, c = ""):
        self.c = c
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = TrieNode(c)
            n = n.children[c]
        n.is_word = True

    def search(self, word: str) -> bool:
        n = self.root
        for c in word:
            if c not in n.children:
                return False
            n = n.children[c]
        return n.is_word
        
    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for c in prefix:
            if c not in n.children:
                return False
            n = n.children[c]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
