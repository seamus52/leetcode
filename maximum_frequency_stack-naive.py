#time: O(n)
#space: O(n)

# 2 dicts:
# - number -> count
# - count -> number

class FreqStack:

    def __init__(self):
        self.vals = {}
        self.counts = {}
        self.insertion_order = []
        

    def push(self, val: int) -> None:
        if val in self.insertion_order:
            self.insertion_order.remove(val)
        self.insertion_order.append(val)
        
        current_cnt = 0
        if val not in self.vals:
            self.vals[val] = 0
        else:
            current_cnt = self.vals[val]
            self.counts[current_cnt].remove(val)
            if self.counts[current_cnt] == 0:
                del self.counts[current_cnt]
        self.vals[val] += 1
        if current_cnt + 1 not in self.counts:
            self.counts[current_cnt + 1] = []
        self.counts[current_cnt + 1].append(val)
        

    def pop(self) -> int:
        max_cnt = max(self.counts.keys())
        value_to_return = self.counts[max_cnt].pop()
        
        if max_cnt - 1 not in self.counts and max_cnt - 1 != 0:
            self.counts[max_cnt - 1] = []
        # bug: implicit insertion order into counts depends on order off arrival of elements
        if max_cnt - 1 != 0:
            if self.counts[max_cnt - 1] == []:
                self.counts[max_cnt - 1].append(value_to_return)
            elif self.insertion_order.index(value_to_return) <= self.counts[max_cnt - 1][-1]:
                self.counts[max_cnt - 1].insert(0, value_to_return)
            else:
                self.counts[max_cnt - 1].append(value_to_return)
                
        self.vals[value_to_return] -= 1
        if self.vals[value_to_return] == 0:
            del self.vals[value_to_return]
            self.insertion_order.remove(value_to_return)
        if self.counts[max_cnt] == []:
            del self.counts[max_cnt]
        print("popped", value_to_return)
        print(self.vals)
        print(self.counts)
        return value_to_return


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
