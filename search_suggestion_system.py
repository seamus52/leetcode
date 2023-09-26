class TrieNode:
    def __init__(self, c=""):
        self.c = c
        self.children = {}
        self.is_word=False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_word = True

    def find(self, word):  # function not need for solution
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def find_prefix(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()

        products.sort()

        for p in products:
            t.add(p)

        prefixes_found = []
        recommendations = {}  # prefix -> list of products matching
        for i in range(1, len(searchWord) + 1):
            if t.find_prefix(searchWord[:i]):
                prefixes_found.append(searchWord[:i])
            recommendations[searchWord[:i]] = []

        for prefix in prefixes_found:
            for p in products:
                if len(recommendations[prefix]) == 3:
                    break
                    
                if p.startswith(prefix):
                    recommendations[prefix].append(p)

        return list(recommendations.values())

