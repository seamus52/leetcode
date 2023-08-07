# maintain dict & majority element (initialize to some value)
# for each element added, compare w/ current majority, update trackers
# return majority element
# time: O(n)
# space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        for n in cnt:
            if cnt[n] > len(nums) / 2:
                return n
