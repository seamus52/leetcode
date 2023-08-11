class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}

        cumsum = 0
        cnt = 0

        for num in nums:
            cumsum += num

            # if complement of cumsum is in the dict, inc cnt with its value
            if cumsum - k in sum_dict:
                cnt += sum_dict[cumsum - k]

            # if cumsum already exists in dict, increase by 1
            if cumsum in sum_dict:
                sum_dict[cumsum] += 1
            # else indicate that it exists (= was found in this iteration)
            else:
                sum_dict[cumsum] = 1

            print(sum_dict)

        return cnt
