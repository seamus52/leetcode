# use monotonic stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        wait_vector = [0] * len(temperatures)

        for current_day, temperature in enumerate(temperatures):
            # If the stack is not empty, there are previous days for which we
            # have not yet seen a warmer day.
            # While the current temperature is warmer than the temperature of prev day
            # (index of the day at the top of the stack):
            while s and temperatures[s[-1]] < temperature:
                prev_day = s.pop()
                # Set answer[prev] equal to the number of days that have passed between
                # prev day and the current day, that is, answer[curr] = prev day - curr.
                wait_vector[prev_day] = current_day - prev_day
            # Push the current index curr onto the stack.
            s.append(current_day)

        return wait_vector
