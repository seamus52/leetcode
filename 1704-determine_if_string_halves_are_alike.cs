public class Solution {
    public bool HalvesAreAlike(string s) {
        int mid = s.Length / 2;
        var a = s.Substring(0, mid);
        var b = s.Substring(mid);

        return VowelCount(a) == VowelCount(b);
    }

    public int VowelCount(string s) {
        int acc = 0;
        var h = new HashSet<char> {'a', 'e', 'i', 'o', 'u'};

        foreach (char c in s) {
            if (h.Contains(char.ToLower(c))) {
                acc += 1;
            }
        }

        return acc;
    }
}
