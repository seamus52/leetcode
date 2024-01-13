public class Solution {
    public bool WordBreak(string s, IList<string> wordDict)
    {
        HashSet<string> words = new(wordDict);
        HashSet<int> visited = new();
        Queue<int> q = new();
        q.Enqueue(0);

        while (q.Count() > 0)
        {
            var start = q.Dequeue();

            if (visited.Contains(start))
            {
                continue;
            }

            visited.Add(start);

            if (start == s.Length)
            {
                return true;
            }

            for (var end = start + 1; end < s.Length + 1; end++)
            {
                if (words.Contains(s.Substring(start, end - start)))
                {
                    if (!visited.Contains(end))
                    {
                        q.Enqueue(end);
                    }
                }
            }
        }

        return false;
    }
}
