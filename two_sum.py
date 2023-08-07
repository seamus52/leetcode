# 1 pass hash table
# Time complexity: O(n). We traverse the list containing nnn elements only once. Each lookup in the table costs only O(1)O(1)O(1) time.
#Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nnn elements.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, n in enumerate(nums):
            if target - n in complement: # check value at 'target - n' key
                return [complement[target - n], i]
            else:
                complement[n] = i # set index = current value at key = current item
        
