class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node  = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                new_node = TrieNode(c)
                node.children[c] = new_node
                node = new_node
        node.leaf = True
        

    def search(self, word: str) -> bool:     
        node  = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.leaf
       

    def startsWith(self, prefix: str) -> bool:
        node  = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
