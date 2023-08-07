class CombinationSum:
    def __init__(self):
        self.combos = [] # collector of genetarted subsets
        self.combo = [] # temporary subset which will be updated as the recursive function executes


    def backtrack(self, nums, start, target):
        if sum(self.combo) == target:
            self.combos.append(self.combo[:]) # copy contents of subset into powerset

        for i in range(start, len(nums)):
            # print(f"i: {i}, subset: {self.subset}, powerset: {self.powerset}")
            # record all subsets that include nums[i]
            self.combo.append(nums[i])
            self.backtrack(nums, i + 1, target)
            # remove nums[i] from the present subset and move further to explore subsets that don't contain nums[i]
            self.combo.pop()


    def combination_sum(self, nums, target):
        self.backtrack(nums, 0, target)
        return self.combos


if __name__ == "__main__":
    nums = [i for i in range(1, 5)]

    ps = CombinationSum()
    combos = ps.combination_sum(nums, 7)

    for s in combos:
        print(s)