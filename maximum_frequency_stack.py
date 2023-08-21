# Time Complexity: O(1) for both push and pop operations.
# Space Complexity: O(N), where N is the number of elements in the FreqStack.

class FreqStack:

    def __init__(self):
        self.freq_of_val = collections.defaultdict(int)
        self.val_of_freq = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        f = self.freq_of_val[val] + 1
        self.freq_of_val[val] = f
        self.max_freq = max(f, self.max_freq)
        self.val_of_freq[f].append(val)

    def pop(self):
        val = self.val_of_freq[self.max_freq].pop()
        self.freq_of_val[val] -= 1
        if not self.val_of_freq[self.max_freq]:
            self.max_freq -= 1

        return val
