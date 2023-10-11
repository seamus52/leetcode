#implemented, which is arguable as it is absolutely not a prefix tree
#time: O(1) assuming no collisions
#space: O(n)
class Trie:

    def __init__(self):
        self.words = set()
        self.prefixes = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        self.prefixes.add(word)
        for i in range(len(word)):
            self.prefixes.add(word[:i])

    def search(self, word: str) -> bool:
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
