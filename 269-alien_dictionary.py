# c: total length of all the words in the input list added together
# time: O(c)
# space: O(1)
from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create data structures
        graph = defaultdict(set)
        in_degree = {c : 0 for c in set("".join(words))}

        # populate data structures
        for first_word, second_word in zip(words, words[1:]):
            for c1, c2 in zip(first_word, second_word):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break
            else: # branch will not execute if stopped by break
            # check that second word isn't a prefix of first word:
            # violates lexographical sorting => no valid ordering
                if len(second_word) < len(first_word): return ""
        
        # pick off nodes with an indegree of 0
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c1 = queue.popleft()
            output.append(c1)
            for c2 in graph[c1]:
                in_degree[c2] -= 1
                if in_degree[c2] == 0:
                    queue.append(c2)
                    
        # not all letters are in output = cycle => no valid ordering
        if len(output) < len(in_degree):
            return ""
        
        # render and return the ordering
        return "".join(output)

