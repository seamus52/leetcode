class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        ops = []

        i = 1
        j = 0
        while i <= n:
            print(i)
            s.append(i)
            ops.append("Push")

            if s[-1] != target[j]:
                s.pop()
                ops.append("Pop")
                j -= 1

            elif s[-1] == target[j] and len(s) == len(target):
                break

            i += 1
            if j < len(target):
                j += 1

        return ops
