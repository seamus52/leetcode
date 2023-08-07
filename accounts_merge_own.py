"""
[
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]
"""
# time: O(edges) + O(n log n) for sort
# space: O(n) n^2 = emails
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def build_graph(accounts):
            graph = {}
            for line in accounts:
                name = line[0]
                emails = line[1:]
                for email in emails:
                    if email not in graph:
                        graph[email] = set()
                    graph[email].update(emails) # this introduces self-cycle
            #remove self-cycle
            for node in graph:
                graph[node].remove(node)
                
            return graph


        def build_email_to_name_map(accounts):
            map = {}
            for line in accounts:
                name = line[0]
                emails = line[1:]
                for email in emails:
                    map[email] = name
            return map


        def dfs(graph, node, visited, emails):
            if node in visited:
                return
            
            visited.add(node)
            emails.append(node)

            for nbr in graph[node]:
                dfs(graph, nbr, visited, emails)


        graph = build_graph(accounts)
        # print(graph)
        email_to_name_map = build_email_to_name_map(accounts)
        # print(email_to_name_map)

        collector = []
        visited = set()
        for node in graph:
            if node not in visited:
                emails = []
                dfs(graph, node, visited, emails)
                name = email_to_name_map[emails[0]]
                collector.append([name, *sorted(emails)])

        return collector
