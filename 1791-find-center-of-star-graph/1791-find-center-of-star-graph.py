class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = dict()
        n = len(edges)
        for i in edges:
            f, t = i
            if f in graph.keys():
                graph[f] += 1
            else:
                graph[f] = 1
            if t in graph.keys():
                graph[t] += 1
            else:
                graph[t] = 1
        for i in graph:
            if graph[i] == n:
                return i