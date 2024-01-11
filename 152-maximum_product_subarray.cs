public class Solution {
    public int MaxProduct(int[] nums)
    {
        int lMax = nums[0];
        int lMin = lMax;
        int gMax = lMax;
        int pMin = lMax;
        int pMax = lMax;

        foreach(int n in nums.Skip(1))
        {
            lMax = new [] {n, n * pMin, n * pMax}.Max();
            lMin = new [] {n, n * pMin, n * pMax}.Min();

            pMax = lMax;
            pMin = lMin;

            gMax = Math.Max(lMax, gMax);
        }

        return gMax;
    }
}
