public class Solution {
    public bool UniqueOccurrences(int[] arr)
    {
        Dictionary<int, int> c = new();
        foreach(int n in arr)
        {
            if (!c.ContainsKey(n))
            {
                c[n] = 0;
            }
            c[n] += 1;
        }

        return c.Values.Count() == new HashSet<int>(c.Values).Count();
    }
}
