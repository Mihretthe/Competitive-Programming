class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxr = 0
        graph = defaultdict(set)
        
        for s, d in roads:
            graph[s].add(d)  
            graph[d].add(s)
        
        for node in range(n):
            for no in range(node + 1, n):
                c = len(graph[node]) + len(graph[no])
                if no in graph[node]:
                    c -= 1
                maxr = max(maxr, c)
        return maxr