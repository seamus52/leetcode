public class Solution {
    int cnt = 0;
    public int ClimbStairs(int n)
    {
        int[] f = new int[n + 1];
        f[0] = 1;
        f[1] = 1;

        for (int i = 2; i <= n; i++)
        {
            f[i] = f[i - 1] + f[i - 2];
        }

        return f[n];
    }
}
