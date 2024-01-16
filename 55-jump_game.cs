public class Solution {
    public bool CanJump(int[] nums) {
        Dictionary<int, bool> memo = new();
        return dfs(0);

        bool dfs(int i)
        {
            if (memo.ContainsKey(i))
            {
                return memo[i];
            }

            if (i == nums.Length - 1)
            {
                memo[i] = true;
                return true;
            }

            if (nums[i] == 0)
            {
                memo[i] = false;
                return false;    
            }

            for (int j = 1; j <= nums[i]; j++)
            {
                if (dfs(i + j))
                {
                    memo[i + j] = true;
                    return true;
                }
            }

            memo[i] = false;
            return false;
        }
    }
}
