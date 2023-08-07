# time: O(n*k)
# space: O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        k_closest = []
        distances = []

        for e in arr:
            distance = abs(x - e)
            # fill the arrays sequentially, until better candidates are found
            if len(k_closest) < k:
                k_closest.append(e)
                distances.append(distance)
            else:
                # if an distance is smaller than the max of k closest so far
                # replace the element
                idx = distances.index(max(distances))
                if distance < max(distances):
                    k_closest.pop(idx)
                    distances.pop(idx)
                    k_closest.append(e)
                    distances.append(distance)
            # print(e, k_closest, distance, distances)

        return k_closest
