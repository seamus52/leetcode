class TreeNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.item_cnt = 0
        self.capacity = k
        self.head = None
        self.tail = self.head
        

    def enQueue(self, value: int) -> bool:
        if self.item_cnt == self.capacity:
            return False

        if self.item_cnt == 0:
            self.head = TreeNode(value)
            self.tail = self.head
        else:
            new_node = TreeNode(value)
            self.tail.next = new_node
            self.tail = self.tail.next
        self.item_cnt += 1
        print(self)
        return True
        

    def deQueue(self) -> bool:
        if self.item_cnt == 0:
            return False
        
        self.head = self.head.next
        self.item_cnt -= 1
        return True
        
    def Front(self) -> int:
        if self.item_cnt == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.item_cnt == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.item_cnt == 0
        
    def isFull(self) -> bool:
        return self.item_cnt == self.capacity

    def __str__(self):
        s = f"({self.tail.val} -> {self.head.val}) : "
        t = self.tail
        while t:
            s += f"{t.val}, "
            t = t.next
        return s
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
