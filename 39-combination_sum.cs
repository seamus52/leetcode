public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        List<IList<int>> combos = new();
        backtrack(0, target, new());
        return combos;

        void backtrack(int start, int remain, Stack<int> combo) {
            if (remain == 0) {
                combos.Add(new List<int>(combo));
                return;
            }
            if (remain < 0) {
                return;
            }

            for (int i = start; i < candidates.Length; i++) {
                combo.Push(candidates[i]);
                backtrack(i, remain - candidates[i], combo);
                combo.Pop();
            }

        }

    }
}
