public class Solution {
    public int Rob(int[] nums)
    {
        Dictionary<int, int> memo = new();
        return rob(0);

        int rob(int i)
        {
            if (memo.ContainsKey(i))
            {
                return memo[i];
            }

            if (i >= nums.Length)
            {
                return 0;
            }

            memo[i] = Math.Max(rob(i + 1), nums[i] + rob(i + 2));
            return memo[i];
        }
    }
}
