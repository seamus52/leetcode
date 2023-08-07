#time: O(1)
#space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        arabic = 0
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        roman = deque(s[:])

        while roman:
            r_value = roman.popleft()
            a_value = values[r_value]

            if len(roman) >= 1:
                if r_value == "I":
                    if roman[0] in "VX":
                        a_value = values[roman.popleft()] - a_value
                elif r_value == "X":
                    if roman[0] in "LC":
                        a_value = values[roman.popleft()] - a_value
                elif r_value == "C":
                    if roman[0] in "DM":
                        a_value = values[roman.popleft()] - a_value

            arabic += a_value

        return arabic
