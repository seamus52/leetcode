# neighbors(word) -> list of words that differ only in one letter
# BFS traverse word -> neighbors
# TLE, neigbors can be optimized: pre-build neighbors dict instead of 
# fully traversing words with every call on neighbors (this will use more space)
# proper solution w/ dict:
# https://leetcode.com/problems/word-ladder/solutions/346920/python3-breadth-first-search/

# time: O(length of each word * words) -> neighbors;
# space: O(1)-ish
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        return self.traverse(beginWord, endWord, wordList)

    
    def traverse(self, begin_word, end_word, word_list):
        visited = set()
        q = deque([(begin_word, 1)])
        steps = 0

        while q:
            w, level = q.popleft()
            if w in visited:
                continue

            visited.add(w)
            
            if w == end_word:
                return level

            for n in self.neighbors(w, word_list):
                q.append((n, level + 1))

        return 0


    def neighbors(self, word, word_list):
        neighbors = []

        for w in word_list:
            divergence = 0

            # this doesn't work if word sizes can differ
            for i in range(len(w)):
                if w[i] != word[i]:
                    divergence += 1
            
            if divergence == 1:
                neighbors.append(w)

        return neighbors
