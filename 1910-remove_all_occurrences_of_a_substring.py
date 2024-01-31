class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        found = True

        while found:
            found = False
            idx = s.find(part)
            if idx != -1:
                s = s[:idx] + s[idx + len(part):]
                found = True

        return s

