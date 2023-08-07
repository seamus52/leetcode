# str -> list, pop, calc/manintain carry
# time: O(n)
# space: O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_bin = int(a, 2)
        b_bin = int(b, 2)

        return bin(a_bin + b_bin)[2:]
        
