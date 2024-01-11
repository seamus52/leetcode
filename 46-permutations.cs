public class Solution {
    public IList<IList<int>> Permute(int[] nums) {
        List<IList<int>> permutations = new();

        void permute(HashSet<int> perm) {
            if (perm.Count == nums.Length) {
                permutations.Add(new List<int>(perm));
            }

            foreach(int n in nums) {
                if (!perm.Contains(n)) {
                    perm.Add(n);
                    permute(perm);
                    perm.Remove(n);
                }
            }
        }

        permute(new());
        return permutations;
    }
}
