# opt 1) brute force: vector length * cartesian product, filter
# optimization: sum with abort upon impossible scenario
# -> TLE

# opt 2) backtrack

# time: O(t*n)
# space: O(t)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # potential optimization
        # nums.sort()

        @functools.lru_cache(maxsize = None)
        def combs(remain):
            if remain == 0:
                return 1

            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combs(remain - num)
                # potential optimization
                # else:
                #     break

            return result

        return combs(target)
