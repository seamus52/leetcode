# edge list -> adj list
# DFS traverse adj list from all nodes, keep track of visited
# store max level (distance from root)
# sort by path length and return root of min length paths
# TLE

# time:
# space: O(node cnt * edge cnt)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if edges == []:
            return [0]

        adj_list = self.edge_list_to_adj_list(edges)

        max_paths = []
        for node in adj_list:
            visited = set()
            path = []
            paths = []
            self.traverse(adj_list, node, visited, path, paths)
            paths.sort(key=lambda x : len(x))
            
            max_path = paths[-1]
            max_paths.append(max_path)

        max_paths.sort(key=lambda x : len(x))
        min_length = len(max_paths[0])

        mht_roots = []
        for p in max_paths:
            if len(p) == min_length:
                mht_roots.append(p[0])

        return mht_roots


    def traverse(self, adj_list, node, visited, path, paths):
        visited.add(node)
        path.append(node)

        visitable_cnt = 0
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visitable_cnt += 1
                self.traverse(adj_list, neighbor, visited, path, paths)
        if visitable_cnt == 0:
            paths.append(path[:])
        
        path.pop()
        

    def edge_list_to_adj_list(self, edge_list):
        tree = {}
        for edge in edge_list:
            if not edge[0] in tree:
                tree[edge[0]] = set()
            if not edge[1] in tree:
                tree[edge[1]] = set()

            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])

        return tree
