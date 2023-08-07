"""
Backtracking general recipe:
- loop over range (start: 0-idx (assuming range starts w/ 1), end: len(elements))
- include i-th element (push)
- recursive call to backtrack (inside loop) on i + 1th element
- remove current (i-th) element (pop)
"""
class PowerSet:
    def __init__(self):
        self.powerset = [] # collector of genetarted subsets
        self.subset = [] # temporary subset which will be updated as the recursive function executes


    def backtrack(self, nums, start):
        self.powerset.append(self.subset[:]) # copy contents of subset into powerset

        for i in range(start, len(nums)):
            # print(f"i: {i}, subset: {self.subset}, powerset: {self.powerset}")
            # record all subsets that include nums[i]
            self.subset.append(nums[i])
            self.backtrack(nums, i + 1)
            # remove nums[i] from the present subset and move further to explore subsets that don't contain nums[i]
            self.subset.pop()


    def subsets(self, nums):
        self.backtrack(nums, 0)
        return self.powerset


if __name__ == "__main__":
    nums = [i for i in range(1, 4)]

    ps = PowerSet()
    subsets = ps.subsets(nums)

    for s in subsets:
        print(s)