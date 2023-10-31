# trick: xor inf the result of xor gives back the original value:
# 5 ^ 2 = 7 => 7 ^ 2 = 5
# time: O(n)
# space: O(n)
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]] * len(pref)

        for i in range(1, len(pref)):
            x = pref[i - 1] ^ pref[i]
            arr[i] = x
            
        return(arr)

