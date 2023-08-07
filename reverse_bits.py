# time: O(n) - bound by 32
# space: O(n)
class Solution:  - bound by 32
    def reverseBits(self, n: int) -> int:
        bits = ["0" for i in range(32)]
        for i, d in enumerate(reversed(bin(n)[2:])):
            bits[i] = d
        return int("".join(bits), 2)
