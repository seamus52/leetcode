class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.q = [0] * k
        self.enq_idx = 0
        self.num_items = 0
        
    def enQueue(self, value: int) -> bool:
        if self.num_items == self.capacity:
            return False
        self.q[(self.enq_idx + self.num_items) % self.capacity] = value
        self.num_items += 1
        return True
        
    def deQueue(self) -> bool:
        if self.num_items == 0:
            return False
        self.enq_idx = (self.enq_idx + 1) % self.capacity
        self.num_items -= 1
        return True
        
    def Front(self) -> int:
        if self.num_items == 0:
            return -1
        return self.q[self.enq_idx]
        
    def Rear(self) -> int:
        if self.num_items == 0:
            return -1
        return self.q[(self.enq_idx + self.num_items - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.num_items == 0

    def isFull(self) -> bool:
        return self.num_items == self.capacity
