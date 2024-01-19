class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the list
        sp = s[::-1]
        l = r = 0

        # reverse individual words
        while r < len(sp):
            while r < len(sp) and sp[r] != " ":
                r += 1

            sp[l:r] = sp[l:r][::-1]
            l = r + 1
            r = l

        for i in range(len(s)):
            s[i] = sp[i]

