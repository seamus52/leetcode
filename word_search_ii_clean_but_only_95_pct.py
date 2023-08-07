class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.leaf = True


    def contains(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.leaf


    def containsPrefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def in_bounds(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])


        def neighbors(r, c):
            neighbors = []
            if in_bounds(r + 1, c): neighbors.append((r + 1, c))
            if in_bounds(r - 1, c): neighbors.append((r - 1, c))
            if in_bounds(r, c + 1): neighbors.append((r, c + 1))
            if in_bounds(r, c - 1): neighbors.append((r, c - 1))
            return neighbors


        def dfs(r, c, collector, visited):
            if (r, c) in visited:
                visited.remove((r, c))
                return
            
            visited.add((r, c))
            collector.append(board[r][c])

            s = "".join(collector)
            print(s)
            if not t.containsPrefix(s):
                visited.remove((r, c))
                collector.pop()
                return

            if t.contains(s):
                present.add(s)

            for nr, nc in neighbors(r, c):
                dfs(nr, nc, collector, visited)

            if (r, c) in visited:
                visited.remove((r, c))
            collector.pop()


        t = Trie()
        for w in words:
            t.add(w)

        present = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, [], set())

        return present
