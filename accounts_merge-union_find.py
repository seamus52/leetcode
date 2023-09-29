from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def union(a, b):
            uf[find(b)] = find(a)

        def find(a):
            uf.setdefault(a, a)
            if uf[a] != a:
                uf[a] = find(uf[a])
            return uf[a]

        uf = {}
        email_to_name = {}
        # dual-purpose loop - see details below
        for line in accounts:
            for email in line[1:]:
                name = line[0]
                email_to_name[email] = name  # populate email_to_name
                union(line[1], email)  # populate up union/find dict
        
        # top-level uf item -> list of dependents on that item
        group_id_to_accounts = {}
        for email in email_to_name: 
            group_id_to_accounts.setdefault(find(email), []).append(email)
        
        # associate each group with a name
        accounts_merged = []
        for group_id, accounts in group_id_to_accounts.items(): 
            accounts_merged.append([email_to_name[group_id]] + sorted(accounts))

        return accounts_merged
