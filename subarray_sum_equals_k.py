#time: O(n)
#space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}  # cumulative sums: sum -> # of occurrences

        cumsum = 0
        cnt = 0

        for num in nums:
            cumsum += num
            # # of times the cumsum - k has occurred already =
            # # of times a subarray with sum k has occurred up to the curr idx
            if cumsum - k in sum_dict:
                cnt += sum_dict[cumsum - k]

            if cumsum in sum_dict:
                sum_dict[cumsum] += 1
            else:
                sum_dict[cumsum] = 1

            print(sum_dict)

        return cnt
