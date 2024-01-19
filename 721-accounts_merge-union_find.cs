public class Solution {
    public IList<IList<string>> AccountsMerge(IList<IList<string>> accounts)
    {
        // uf infrastructure
        Dictionary<string, string> uf = new();

        void union(string a, string b)
        {
            uf[find(b)] = find(a);
        }

        string find(string a)
        {
            if (!uf.ContainsKey(a))
            {
                uf[a] = a;
            }

            if (uf[a] != a)
            {
                uf[a] = find(uf[a]);
            }

            return uf[a];
        }

        // build uf dict
        foreach(List<string> line in accounts)
        {
            string groupParentAccount = line[1];
            for(int i = 1; i < line.Count(); i++)
            {
                union(groupParentAccount, line[i]);
            }
        }

        // print uf - verification of uf infrastructure and build
        // foreach(List<string> line in accounts)
        // {
        //     for(int i = 1; i < line.Count(); i++)
        //     {
        //         Console.WriteLine(line[i] + " is a child of " + find(line[i]));
        //     }
        // }

        // build email -> name dict
        // could be coalesced wit the uf build loop, keeping separate for readability
        Dictionary<string, string> emailToName = new();
        foreach(List<string> line in accounts)
        {
            string name = line[0];
            for(int i = 1; i < line.Count(); i++)
            {
                emailToName[line[i]] = name;
            }
        }

        // build parent acct -> set of related accts dict
        Dictionary<string, HashSet<string>> accountsMerged = new();
        foreach(string email in emailToName.Keys)
        {
            string groupParentAccount = find(email);
            if (!accountsMerged.ContainsKey(groupParentAccount)){
                accountsMerged[groupParentAccount] = new();
            }
            accountsMerged[groupParentAccount].Add(email);
        }

        // assemble output:
        // sorted list of related accounts, prefixed by name that maps to uf parent acct
        List<IList<string>> output = new();
        foreach (string groupParentAccount in accountsMerged.Keys)
        {
            List<string> a = new List<string>{emailToName[groupParentAccount]};
            List<string> b = new List<string>(accountsMerged[groupParentAccount]);
            Console.WriteLine("[{0}]", string.Join(", ", b));
            b.Sort(StringComparer.Ordinal);  // specific sort order is needed to pass tests
            Console.WriteLine("[{0}]", string.Join(", ", b));
            a.AddRange(b);
            output.Add(a);
        }

        return output;
    }
}
