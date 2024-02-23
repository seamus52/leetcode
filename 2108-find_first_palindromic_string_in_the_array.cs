public class Solution
{
    public string FirstPalindrome(string[] words)
    {
        foreach(string w in words)
        {
            char[] wChArr = w.ToCharArray();
            Array.Reverse(wChArr);
            if (w == new string(wChArr))
            {
                return w;
            }
        }

        return "";
    }
}
