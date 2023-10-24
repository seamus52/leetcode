# time: O(n log n) - sort dominates
# space: O(n)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for entry in logs:
            if entry[-1].isdigit():
                digit_logs.append(entry)
            else:
                letter_logs.append(entry)

        letter_logs.sort(key=lambda x: (x[x.index(" "):], x[:x.index(" ")]))

        return letter_logs + digit_logs
