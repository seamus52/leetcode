public class Solution {
    public int[] AsteroidCollision(int[] asteroids) {
        bool CanCollide(int a, int b){
            return (a > 0 && b < 0);
        }

        List<int> s = new();

        Queue<int> ast = new(asteroids);

        foreach(int asteroid in ast)
        {
            s.Add(asteroid);

            while (s.Count() >= 2 && CanCollide(s[s.Count() - 2], s[s.Count() - 1]))
            {
                int b = s[s.Count() - 1];
                s.RemoveAt(s.Count() - 1);
                int a = s[s.Count() - 1];
                s.RemoveAt(s.Count() - 1);

                if (a > Math.Abs(b))
                {
                    s.Add(a);
                }
                else if (a < Math.Abs(b))
                {
                    s.Add(b);
                }
            }
        }

        return s.ToArray();
    }
}
