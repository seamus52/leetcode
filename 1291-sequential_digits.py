class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        ans = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(len(digits) + 1 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans

