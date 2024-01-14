public class Solution {
    public int MaxProfit(int[] prices)
    {
        int minPrice = prices[0];
        int maxProfit = Int32.MinValue;

        foreach(int n in prices)
        {
            if (n < minPrice)
            {
                minPrice = n;
            }
            else
            {
                maxProfit = Math.Max(maxProfit, n - minPrice);
            }
        }

        return maxProfit;
    }
}
