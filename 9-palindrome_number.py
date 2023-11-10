# time: O(n)
# space: O(n) - O(1) solution would compare w/ 2 ptrs startinhg from each end, meeting halfway
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
