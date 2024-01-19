class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        combos = []
        
        for i in range(len(arr)):
            for j in range(1, len(arr) + 1):
                elem = []
                if i + j < len(arr) + 1:
                    elem.extend(arr[i:i + j])
                if elem:
                    combos.append(elem[:])

        # print(combos)
        return sum([min(combo) for combo in combos]) % (10 ** 9 + 7)

