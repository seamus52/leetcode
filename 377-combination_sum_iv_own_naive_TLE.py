# opt 1) brute force: vector length * cartesian product, filter
# optimization: sum with abort upon impossible scenario
# -> TLE

# opt 2) backtrack

# time: O(n!) - product dominates
# space: O(n!) - product dominates
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cnt = 0
        for i in range(1, target + 1):
            for combo in itertools.product(nums, repeat=i):
                # print(combo)
                if sum(combo) == target:
                    cnt += 1

        return cnt

