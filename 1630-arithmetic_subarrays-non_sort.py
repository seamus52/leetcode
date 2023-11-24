# time: O(n * m)
# space: O(1)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        collector = []
        for s, e in zip(l, r):
            subseq = nums[s:e + 1]
            min_elem = min(subseq)
            max_elem = max(subseq)

            # if the diff between max and min elem is not integer
            # we conclude that the subseq is not arithmetic
            # optimization only: the code works fine without this
            if (max_elem - min_elem) % (len(subseq) - 1) != 0:
                collector.append(False)
                continue

            # diff of arithmetic seq: (max + min) / n
            diff = (max_elem - min_elem) / (len(subseq) - 1)
            
            subseq_set = set(subseq)
            curr = min_elem + diff
            while curr < max_elem:
                if curr not in subseq_set:
                    collector.append(False)
                    break
                curr += diff
            else:
                collector.append(True)
            
        return collector

