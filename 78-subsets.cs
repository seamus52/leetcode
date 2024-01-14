public class Solution {
    public IList<IList<int>> Subsets(int[] nums)
    {
        List<IList<int>> combos = new();
        dfs(0, new());
        return combos;

        void dfs(int start, List<int> combo)
        {
            if (combo.Count > nums.Length)
            {
                return;
            }

            combos.Add(new List<int>(combo));

            for (int i = start; i < nums.Length; i++)
            {
                combo.Add(nums[i]);
                dfs(i + 1, combo);
                combo.RemoveAt(combo.Count() - 1);
            }
        }
    }
}
