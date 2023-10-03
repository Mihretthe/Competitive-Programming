class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph = {}
        for (numerator, denominator), value in zip(equations, values):
            if numerator not in graph:
                graph[numerator] = {}
            if denominator not in graph:
                graph[denominator] = {}
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        # Perform DFS for each query
        results = []
        for query in queries:
            start, end = query
            if start not in graph or end not in graph:
                results.append(-1.0)
            elif start == end:
                results.append(1.0)
            else:
                visited = set()
                result = self.dfs(graph, start, end, visited)
                results.append(result)

        return results

    def dfs(self, graph, start, end, visited):
        if start == end:
            return 1.0

        visited.add(start)

        for neighbor, value in graph[start].items():
            if neighbor not in visited:
                result = self.dfs(graph, neighbor, end, visited)
                if result != -1.0:
                    return value * result

        return -1.0