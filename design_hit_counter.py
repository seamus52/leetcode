# hit time: O(1)
# hit space: O(n)
# getHits time: O(n)
# getHits space: O()
class HitCounter: O(1)

    def __init__(self):
        self.hit_cnt = defaultdict(int)
        

    def hit(self, timestamp: int) -> None:
        self.hit_cnt[timestamp] += 1

        
    def getHits(self, timestamp: int) -> int:
        hits_in_last_5min = 0
        for i in range(timestamp - 299, timestamp + 1):
            # print(f"{i}: {self.hit_cnt[i]}")
            hits_in_last_5min += self.hit_cnt[i]

        return hits_in_last_5min

        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
