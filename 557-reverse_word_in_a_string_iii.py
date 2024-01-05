class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        for w in s.split():
            output += " " + w[::-1]

        return output[1:]
    
