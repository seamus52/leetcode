class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        
        for first_idx in range(len(nums)):
            second_idx = first_idx + 1
            third_idx = len(nums) - 1
            while second_idx <= third_idx:
                s = nums[first_idx] + nums[second_idx] + nums[third_idx]
                if first_idx != second_idx and second_idx != third_idx \
                and first_idx != third_idx and s == 0:
                    triplets.add((nums[first_idx], nums[second_idx], nums[third_idx]))
                    second_idx += 1
                    third_idx -= 1
                elif s > 0:
                    third_idx -=1
                else:
                    second_idx += 1

        return triplets
        
