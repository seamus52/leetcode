from string import ascii_lowercase
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # count of each English lowercase char (including 0s)
        char_cnt = {}
        for c in ascii_lowercase:
            char_cnt.setdefault(c, 0)
        for c in s:
            char_cnt[c] += 1


        buttons = {}
        for i in (range(9)):
            buttons.setdefault(i, [])

        # assign chars to buttons by frequency:
        # most frequent is accessible with lowest # of presses
        # (lower pos in the dict value (list))
        key_space = 9
        i = 1
        for char, cnt in sorted(char_cnt.items(), key=lambda x: x[1], reverse=True):
            ptr = i % key_space
            buttons[ptr].append(char)
            i += 1

        # score
        res = 0
        for c in s:
            for b in buttons:
                if c in buttons[b]:
                    res += buttons[b].index(c) + 1

        return res
