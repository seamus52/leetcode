# Clarification:
# Input:
# "TAUXXTAUXXTAUXXTAUXXTAUXX"
# "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# Expected result:
# "TAUXX"
# time: O(n)
# space: O(n)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0] != str2[0]:
            return ""

        candidate = ""
        gcd = ""
        for c in str1:
            candidate += c
            if candidate * (len(str1) // len(candidate)) == str1 \
                and candidate * (len(str2) // len(candidate)) == str2:
                gcd = candidate

        return gcd

