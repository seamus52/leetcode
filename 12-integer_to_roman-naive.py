# time: O(n) - perhaps closer to O(1), since input size is bounded
# space O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = hundreds = tens = ones = 0
        if num >= 1000:
            thousands = num // 1000
            num -= thousands * 1000
        
        if num >= 100:
            hundreds = num // 100
            num -= hundreds * 100

        if num >= 10:
            tens = num // 10
            num -= tens * 10

        if num >= 1:
            ones = num // 1
            num -= ones * 1

        # print(thousands, hundreds, tens, ones)
        
        # thousands
        num_s = "M" * thousands

        # hundreds
        if hundreds <= 3:
            num_s += "C" * hundreds
        elif hundreds == 4:
            num_s += "CD"
        elif hundreds == 5:
            num_s += "D"
        elif hundreds < 9:
            num_s += "D" + (hundreds - 5) * "C"
        elif hundreds == 9:
            num_s += "CM"

        # tens
        if tens <= 3:
            num_s += "X" * tens
        elif tens == 4:
            num_s += "XL"
        elif tens == 5:
            num_s += "L"
        elif tens < 9:
            num_s += "L" + (tens - 5) * "X"
        elif tens == 9:
            num_s += "XC"

        # ones
        if ones <= 3:
            num_s += "I" * ones
        elif ones == 4:
            num_s += "IV"
        elif ones == 5:
            num_s += "V"
        elif ones < 9:
            num_s += "V" + (ones - 5) * "I"
        elif ones == 9:
            num_s += "IX"

        return num_s
