public class Solution {
    public int MaxSubArray(int[] nums)
    {
        int localMax = nums[0];
        int globalMax = localMax;

        foreach(int n in nums.Skip(1))
        {
            localMax = Math.Max(n, localMax + n);
            globalMax = Math.Max(localMax, globalMax);
        }
        return globalMax;
    }
}
