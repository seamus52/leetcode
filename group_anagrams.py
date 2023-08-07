#time: O(n)
#space: O(n)
# current solution works w/ Counter
# a simpler solution is categorize by sorted string
# ans = collections.defaultdict(list)
#        for s in strs:
#            ans[tuple(sorted(s))].append(s)
#        return ans.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            char_cnt = frozenset(Counter(word).items())
            if char_cnt not in anagrams:
                anagrams[char_cnt] = []
            anagrams[char_cnt].append(word)

        return anagrams.values()
