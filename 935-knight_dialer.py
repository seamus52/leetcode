d = {
    0:[4,6],
    1:[6,8],
    2:[7,9],
    3:[4,8],
    4:[0,3,9],
    5:[],
    6:[0,1,7],
    7:[2,6],
    8:[1,3],
    9:[2,4]
    }

class Solution:
    def knightDialer(self, n: int) -> int:
        nums = [1] * 10

        for i in range(1, n):
            next_nums = [0] * 10
            for idx in range(len(nums)):
                for v in d[idx]:
                    next_nums[v] += nums[idx]
            nums = next_nums
        
        return sum(nums) % (10 ** 9 + 7)
