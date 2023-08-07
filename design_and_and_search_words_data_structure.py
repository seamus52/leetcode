# time:
# - add: O(n)
# - search: O(26^m) - in case of many wildcards
# space:
# - add: O(n)
# - search: O(26^m) recursive stack for wildcards
class TrieNode:
    def __init__(self, c=""):
        self.c = c
        self.children = {}
        self.is_leaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                new_node = TrieNode(c)
                node.children[c] = new_node
                node = new_node
        node.is_leaf = True
        

    def search(self, word: str) -> bool:
        def dfs(node, index):
            print(node.c, index)
            # case 1: matched util the end of the word
            if index == len(word):
                return node.is_leaf

            # case 2: chat at index is wildcard
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True

            # case 3: chat at index is regular character
            if word[index] in node.children:
                node = node.children[word[index]]
                return dfs(node, index + 1)

            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
