# time: O(n choose k)
# space: O(k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return itertools.combinations(range(1, n + 1), k)
        collector = []
        def backtrack(remaining, combo, next):
			# solution found
            if remaining == 0:
                collector.append(combo[:])
            else:
				# iterate through all possible candidates
                for i in range(next, n + 1):
					# add candidate
                    combo.append(i)
					#backtrack
                    backtrack(remaining - 1, combo, i+1)
					# remove candidate
                    combo.pop()
            
        backtrack(k, [], 1)
        return collector
        
