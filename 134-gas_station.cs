public class Solution {
    public int CanCompleteCircuit(int[] gas, int[] cost) {
        if (gas.Sum() < cost.Sum())
        {
            return -1;
        }

        int startAt = 0;
        int level = 0;

        for (int i = 0; i < gas.Length; i++)
        {
            level += gas[i] - cost[i];
            if (level < 0)
            {
                startAt = i + 1;
                level = 0;
            }
        }

        return startAt;
    }
}
