# solution:
# implement union find
# set up UF relationships between synonyms
# go through d keys
# call find(), add to (new) groups dict:
#   find(k) return value (= will identify group) -> k 
# process groups' values to construct sentences
# use itertools product to create possible combinations\
# time: O(n*m) - union find dominates (as graph)
# space: O(n*m) - stack depth of union find (as graph)

from collections import defaultdict
from itertools import product
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # Implement UF
        d = {}

        def union(a, b):
            d[find(b)] = find(a)

        def find(a):
            d.setdefault(a, a)
            if d[a] != a:
                d[a] = find(d[a])
            return d[a]

        # set up UF relationships between synonyms
        for a, b in synonyms:
            union(a, b)

        # UF tests        
        # print(d)
        # print(find("joy") == find("sorrow"))
        # print(find("cheerful") == find("joy"))

        # print(d.keys())
        # print(find("joy"))
        # print(find("happy"))

        groups = defaultdict(set)
        for k in d.keys():
            groups[find(k)].add(k)

        sentences = []
        sentence_template = []
        # create cartesian product using of groups
        for word in text.split(" "):
            if word not in d.keys():
                sentence_template.append([word])
            else:
                group_id = find(word)
                sentence_template.append(list(groups[group_id]))
        # print(sentence_template)

        for instance in product(*sentence_template):
            # print(instance)
            sentences.append(" ".join(instance))

        return sorted(sentences)
