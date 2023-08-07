class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    # time: O(n)
    # space: O(n)
    # can also optimize for fast pop by doing shuffling on push
    def pop(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        
        item_to_return = self.s2.pop()

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

        return item_to_return

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
