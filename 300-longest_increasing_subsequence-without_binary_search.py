class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for n in nums[1:]:
            if n > sub[-1]:
                sub.append(n)
            else:
                i = 0
                while n > sub[i]:
                    i += 1
                sub[i] = n

        return len(sub)

