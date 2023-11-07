from heapq import heappush, heappop
class SeatManager:

    def __init__(self, n: int):
        self.reservations = [x for x in range(1, n + 1)]
        # heapify(self.reservations)
        # print(self.reservations)

    def reserve(self) -> int:
        return heappop(self.reservations)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.reservations, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
