# time: O(log n) - maintain sorted container
# space: O(n)
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.values = SortedList()
        

    def addNum(self, num: int) -> None:
        self.values.add(num)
        

    def findMedian(self) -> float:
        if len(self.values) % 2 != 0:
            return self.values[len(self.values) // 2]
        else:
            return (self.values[len(self.values) // 2 - 1] + self.values[len(self.values) // 2]) / 2

        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
