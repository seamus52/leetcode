# time: O(n) as string
# space: O(n) as string
class Solution:
    def reverse(self, x: int) -> int:
        max_bound = 2 ** 31 - 1
        min_bound = -2 ** 31

        sign = 1
        if x < 0: sign = -1

        if sign < 0:
            rev_x = "".join(str(x * -1)[::-1])
            rev_x = "-" + rev_x
        else:
            rev_x = "".join(str(x)[::-1])

        if int(rev_x) > max_bound or int(rev_x) < min_bound:
            return 0
        return int(rev_x)
