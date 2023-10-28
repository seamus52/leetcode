# time: worse than ~O(n!), bettter then O(n*n!)
# space: O(n) - recursive call stack, not counting the result gathered
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutation):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return

            for i in range(len(nums)):
                if nums[i] not in permutation:
                    permutation.append(nums[i])
                    backtrack(permutation)
                    permutation.pop()
        
        permutations = []
        backtrack([])
        return permutations
