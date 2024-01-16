public class Solution {
    public int LeastInterval(char[] tasks, int n)
    {
        Dictionary<char, int> taskCount = new();
        foreach (char c in tasks)
        {
            if (!taskCount.ContainsKey(c))
            {
                taskCount[c] = 0;
            }
            taskCount[c] += 1;
        }
        int maxTaskCount = taskCount.Values.Max();

        int numTasksWithMaxCount = 0;
        foreach (int v in taskCount.Values)
        {
            if (v == maxTaskCount)
            {
                numTasksWithMaxCount += 1;
            }
        }

        // case 1: enough slots
        int c1 = tasks.Length;

        // case 2: not enough slots
        int c2 = (n + 1) * (maxTaskCount - 1) + numTasksWithMaxCount;
        
        return Math.Max(c1, c2);
    }
}
