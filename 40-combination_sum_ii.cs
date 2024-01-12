public class Solution {
    public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
        Array.Sort(candidates);

        List<IList<int>> combos = new();
        backtrack(0, target, new());
        return combos;

        void backtrack(int start, int remain, Stack<int> combo)
        {
            if (remain == 0)
            {
                combos.Add(new List<int>(combo));
                return;
            }
            if (remain < 0)
            {
                return;
            }

            for (int i = start; i < candidates.Length; i++)
            {
                if (i > start && candidates[i] == candidates[i - 1])
                {
                    continue;
                }
                combo.Push(candidates[i]);
                backtrack(i + 1, remain - candidates[i], combo);
                combo.Pop();
                
            }
        }
    }
}
