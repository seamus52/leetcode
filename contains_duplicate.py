# use map, Counter (may pass) but is inefficient here as it cannot stop before all elements are enumerated
# since it is still O(n), not too worried

# time: O(n)
# space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for v in cnt.values():
            if v >= 2:
                return True
    
        return False
