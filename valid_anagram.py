from collections import Counter
# time O(n)
# space O(1) -> just minimum extra space is used for hash table
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)

# alternative: sorting, time O(n log n) [dominates over n], space O(1) with in-place sort
