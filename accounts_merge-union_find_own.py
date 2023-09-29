from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = {}

        def union(a, b):
            uf[find(b)] = find(a)

        def find(a):
            uf.setdefault(a, a)
            if uf[a] != a:
                uf[a] = find(uf[a])
            return uf[a]

        # build list_of_emails -> name map
        emails_to_name = {}
        for line in accounts:
            acct_name = line[0]
            acct_emails = line[1:]
            emails_to_name[tuple(acct_emails)] = acct_name

        # group emails together according to spec (separate loop for clarity)
        for line in accounts:
            find(line[1])
            for acct in line[1:]: # make sure this is OK
                union(line[1], acct)

        # test uf
        # print(uf)
        # print(find("john00@mail.com"))
        # print(find("mary@mail.com"))
        # print(find("johnnybravo@mail.com"))
        # for v in set(uf.values()):
        #     print(v)

        # disinct groups -> names, using top-level uf entry
        group_to_name = {}
        for acct_grp_id in set(uf.values()):
            for line in accounts:
                if find(acct_grp_id) in line:
                    acct_name = line[0]
                    group_to_name[acct_grp_id] = acct_name

        print(len(group_to_name))
        print(group_to_name)

        # group -> accts
        accts_of_group_id = defaultdict(set)
        for line in accounts:
            for acct in line[1:]:
                accts_of_group_id[find(line[1])].add(acct)

        # print(len(accts_of_group_id))
        
        accounts_merged = []
        for group_id in group_to_name:
            if accts_of_group_id[group_id]:
                accounts_merged.append([group_to_name[group_id]]
                + sorted(accts_of_group_id[group_id]))

        return accounts_merged
