public class Solution {
    public IList<IList<int>> CombinationSum3(int k, int n) {
        List<IList<int>> combos = new();
        backtrack(1, n, new());
        return combos;

        void backtrack(int start, int remain, Stack<int> combo) {
            if (combo.Count == k && remain == 0) {
                combos.Add(new List<int>(combo));
                return;
            }
            if (combo.Count > k || remain < 0) {
                return;
            }

            for (int num = start; num < 10; num++) {
                combo.Push(num);
                backtrack(num + 1, remain - num, combo);
                combo.Pop();
            }
        }
    }
}
