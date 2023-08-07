# Time Complexity: O(1) for both push and pop operations.
# Space Complexity: O(N), where N is the number of elements in the FreqStack.

class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.counts = collections.defaultdict(list) # initizalizes counts as []
        self.max_freq = 0

    def push(self, val):
        f = self.freq[val] + 1 # in Counter, count of a missingelement is 0
        self.freq[val] = f
        self.max_freq = max(f, self.max_freq)
        self.counts[f].append(val)

    def pop(self):
        val = self.counts[self.max_freq].pop()
        self.freq[val] -= 1
        if self.counts[self.max_freq] == []:
            self.max_freq -= 1

        return val
