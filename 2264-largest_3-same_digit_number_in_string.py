# time: O(n)
# space: O(1)
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_candidate = "-1"
        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2]:
                if int(num[i - 2:i + 1]) > int(max_candidate):
                    max_candidate = num[i - 2:i + 1]

        return max_candidate if max_candidate != "-1" else ""

