public class Solution {
    public int CombinationSum4(int[] nums, int target)
    {
        var memo = new Dictionary<int, int>();
        return dfs(target);

        int dfs(int remain)
        {
            if (memo.ContainsKey(remain)) {
                return memo[remain];
            }

            if (remain == 0) {
                return 1;
            }
            if (remain < 0)
            {
                return 0;
            }

            int cnt = 0;
            foreach(int num in nums)
            {
                cnt += dfs(remain - num);
            }

            memo[remain] = cnt;

            return cnt;
        }
    }
}
