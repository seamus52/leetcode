#time: O(n)
#space: O(n)

class Solution:
    # Two asteroids can collide if:
    # 1. the asteroid on the left is traveling right (positive), and
    # 2. the asteroid on the right is traveling left (negative).
    def can_collide(self, a: int, b: int) -> bool:
        return a > 0 and b < 0

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for asteroid in asteroids:
            s.append(asteroid)

            while len(s) >= 2 and self.can_collide(s[-2], s[-1]):
                b = s.pop()
                a = s.pop()

                # Append the larger of the two asteroids or neither if they are the same size.
                if a > abs(b):
                    s.append(a)
                elif abs(b) > a:
                    s.append(b)

        return s
