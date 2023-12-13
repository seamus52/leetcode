# itertools.product
# time: O(n!)
# space: O(n!)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        num_to_letter = {
            2 : ("a", "b", "c"),
            3 : ("d", "e", "f"),
            4 : ("g", "h", "i"),
            5 : ("j", "k", "l"),
            6 : ("m", "n", "o"),
            7 : ("p", "q", "r", "s"),
            8 : ("t", "u", "v"),
            9 : ("w", "x", "y", "z")
        }
        
        sets_for_digits = []
        for d in digits:
           sets_for_digits.append(num_to_letter[int(d)])

        combinations = []
        for combo in itertools.product(*sets_for_digits):
            combinations.append("".join(combo))

        return combinations
