public class Solution
{
    public int MajorityElement(int[] nums)
    {
        Dictionary<int, int> d = new();
        foreach(int n in nums)
        {
            if (!d.ContainsKey(n))
            {
                d[n] = 1;
            }
            else
            {
                d[n] += 1;
            }
        }

        return d.Aggregate((l, r) => l.Value > r.Value ? l : r).Key;
    }
}
