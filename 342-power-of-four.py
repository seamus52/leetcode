class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for x in range(15):
            p = 4 ** x
            if n == p:
                return True
            if n < p:
                break
            
        return False

