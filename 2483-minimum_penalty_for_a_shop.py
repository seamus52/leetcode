class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr_pen = customers.count("Y")
        min_pen = curr_pen
        min_idx = 0

        for i in range(len(customers)):
            if customers[i] == "Y":
                curr_pen -= 1
            else:
                curr_pen += 1
            if curr_pen < min_pen:
                min_idx = i + 1
                min_pen = curr_pen

        return min_idx
        
