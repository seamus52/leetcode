class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        if 0 in s:
            s.remove(0)

        cnt = 0
        while s:
            min_elem = min(s)
            new_s = set()
            for e in s:
                e -= min_elem
                if e != 0:
                    new_s.add(e)
                s = new_s
            cnt += 1

        return cnt
