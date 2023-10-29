class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        

        perimeter = sum(matchsticks)
        side = perimeter // 4
        sides = [0] * 4

        if side * 4 != perimeter:  # 1. early termination for impossible case
            return False
        
        # facilitates 2. early termination for impossible case
        matchsticks.sort(reverse=True)
        
        return backtrack(0)
