from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # return Counter(arr).most_common(1)[0][0]
        cnt = 1
        max_cnt = 1
        max_item = arr[0]

        for i, e in enumerate(arr[1:], 1):
            if e == arr[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
                max_item = e

        return max_item

