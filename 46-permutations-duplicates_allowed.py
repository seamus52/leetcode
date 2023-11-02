# this rewrite allows repeated elements by tracking visited indexes
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute(perm):
            if len(perm) == len(nums):
                perms.append(perm[:])

            for i, n in enumerate(nums):
                if i not in visited:
                    visited.add(i)
                    perm.append(n)
                    permute(perm)
                    perm.pop()
                    visited.remove(i)

        visited = set()
        perms = []
        permute([])
        return perms
