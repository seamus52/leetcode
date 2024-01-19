from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        s = ""

        # consume the numbers that come in pairs, high to low
        keys_with_zeros = []
        for k in sorted(c.keys(), reverse=True):
            while c[k] >= 2:
                s += k
                c[k] -= 2
                if c[k] == 0:
                    keys_with_zeros.append(k)

        # clean up dict: remove keys for which all occurrences are already used
        for k in keys_with_zeros:
            del c[k]
    
        mid_num = ""
        # consume the single highest number
        for k in sorted(c.keys(), reverse=True):
            mid_num = k
            c[k] -= 1
            break  # take the 1st occurrence

        # print(f"before: {s}")
        # adjust for leading/trailing 0's
        zeros_consumed = 0
        while s and s[0] == "0":
            s = s[1:]
            zeros_consumed += 1
        # print(f"after: {s}")

        if s == "" and zeros_consumed > 0 and not mid_num:
            return "0"

        return s + mid_num + s[::-1]

