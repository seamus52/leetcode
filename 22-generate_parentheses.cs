public class Solution {
    public IList<string> GenerateParenthesis(int n)
    {
        List<string> ans = new();
        dfs(0, 0, "");
        return ans;

        void dfs(int open, int close, string s)
        {
            if (s.Length == 2 * n)
            {
                ans.Add(s);
                return;
            }

            if (open < n)
            {
                dfs(open + 1, close, ")" + s);
            }
            if (close < open)
            {
                dfs(open, close + 1, "(" + s);
            }
        }
    }
}
