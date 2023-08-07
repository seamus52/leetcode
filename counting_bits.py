# time: O(N)
# space: O(N)

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        
        for num in range(n + 1):
            bits.append(bin(num).count('1'))

        return bits

