class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(list("aeiouAEIOU"))

        vowels_in_s = []

        s_as_list = list(s)
        for c in s_as_list:
            if c in vowels:
                vowels_in_s.append(c)
        
        vowels_in_s.sort(reverse=True)

        for i, c in enumerate(s_as_list):
            if c in vowels:
                s_as_list[i] = vowels_in_s.pop()

        return "".join(s_as_list)

