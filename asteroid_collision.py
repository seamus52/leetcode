#time: O(n)
#space: O(n)

# Case 1 (++): both asteroids moving right: no collision
# Case 2 (--): both asteroids moving left: no collision
# Case 3 (-+): left asteroid moving left, right asteroid moving right: no collision
# Case 4 (+-): left asteroid moving right, right asteroid moving left: collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        
        for a in asteroids:
			# if stack not empty, need to check if case 4
            while s and s[-1] > 0 and a < 0:
				# determine which asteroids are exploding
                if abs(s[-1]) < abs(a):
                    s.pop()
					# considered asteroid might still destroy others 
                    # so continue checking
                    continue
                elif abs(s[-1]) == abs(a):
                    s.pop()
                break
			# if nothing on the stack/cases 1-3, just append
            else:
                s.append(a)
        return s
                    
