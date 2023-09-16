class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        a = [0] * n
        def bfs(i):
            if a[i]:
                return True
            
            q = deque([i])
            a[i] = -1
            while q:
                i = q.popleft()
                for j in graph[i]:
                    if a[i] == a[j]:
                        return False
                    elif not a[j]:
                        q.append(j)
                        a[j]  = -1 * a[i]
            return True
            
        for i in range(n):
            if not bfs(i):
                return False
        return True
            
        
            
            