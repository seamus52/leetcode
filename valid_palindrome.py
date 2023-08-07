#time: O(n)
#space: O(n)
from string import ascii_letters

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = [c.lower() for c in s if c in ascii_letters or c in digits]
        # for i in range(1, len(cleaned) // 2 + 1):
        #     if cleaned[i-1] != cleaned[-i]:
        #         print(i, -i)
        #         return False
        
        # return True
        
        # simple solution
        return cleaned == cleaned[::-1]
