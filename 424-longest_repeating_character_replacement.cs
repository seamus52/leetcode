public class Solution {
    public int CharacterReplacement(string s, int k)
    {
        int l = 0;
        int maxLength = 0;
        Dictionary<char, int> freq = new();

        for (int r = 0; r < s.Length; r++)
        {
            if (!freq.ContainsKey(s[r]))
            {
                freq[s[r]] = 0;
            }
            freq[s[r]] += 1;

            int currLength = r - l + 1;
            if (currLength - freq.Values.Max() > k)
            {
                freq[s[l]] -= 1;
                l += 1;
            }
            else
            {
                maxLength = Math.Max(maxLength, currLength);
            }
        }

        return maxLength;
    }
}
