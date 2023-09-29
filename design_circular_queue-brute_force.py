# descriptioj is poor, interpret it literally: no op on False conditions!
# time: O(n^2) worst case mutations
# space O(n)
class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.q = []
        
    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.capacity:
            print(self.q)
            return False
        self.q.insert(0, value)
        print(self.q)
        return True
        
    def deQueue(self) -> bool:
        if not self.q:
            return False
        self.q.pop()
        return True
        
    def Front(self) -> int:
        if self.q:
            return self.q[-1]
        return -1
        
    def Rear(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.capacity
