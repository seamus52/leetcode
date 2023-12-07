# time: O(n)
# space: O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        seed = 0
        acc = 0
        full_loops = n // 7
        partial_loop = n % 7
        for _ in range(full_loops):
            seed += 1
            daily_increment = seed
            for _ in range(7):
                acc += daily_increment
                daily_increment += 1

        seed += 1
        daily_increment = seed
        for _ in range(partial_loop):
            acc += daily_increment
            daily_increment += 1

        return acc

