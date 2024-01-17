public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        Stack<int> s = new();
        int[] waitVector = new int[temperatures.Length];  // auto-initialized to 0

        for(int currDay = 0; currDay < temperatures.Length; currDay++)
        {
            int t = temperatures[currDay];

            while (s.Count() > 0 && temperatures[s.Peek()] < t)
            {
                int prevDay = s.Pop();
                waitVector[prevDay] = currDay - prevDay;
            }
            s.Push(currDay);
        }

        return waitVector;
    }
}
