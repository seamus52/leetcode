public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites)
    {
        // build graph
        Dictionary<int, HashSet<int>> graph = new();
        for (int i = 0; i < numCourses; i++)
        {
            graph[i] = new();
        }
        foreach(int[] prereq in prerequisites)
        {
            var (a, b) = Tuple.Create(prereq[0], prereq[1]);
            graph[b].Add(a);
        }

        HashSet<int> gray = new();
        HashSet<int> black = new();
        bool cycle = false;

        for (int i = 0; i < numCourses; i++)
        {
            dfs(i);
            if (cycle)
            {
                return false;
            }
        }

        return true;

        void dfs(int node)
        {
            if (black.Contains(node))
            {
                return;  // already visited
            }

            if (gray.Contains(node))
            {
                cycle = true;
                return;
            }

            gray.Add(node);

            foreach(int nbr in graph[node]) {
                dfs(nbr);
            }

            gray.Remove(node);
            black.Add(node);
        }

        return false;
    }
}
