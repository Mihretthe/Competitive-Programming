class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = dict()
        for i in range(n):
            graph[i] = []  
        for i in edges:
            a, b = i
            graph[a].append(b)      
            graph[b].append(a)
        
        
        visited = set()
        used = set()
        def dfs(source):
            nonlocal visited
            nonlocal destination
            nonlocal graph 
            
            visited.add(source)
            if source == destination:
                return True
            
            for i in graph[source]:
                if i not in visited and i not in used:
                    used.add(i)
                    if dfs(i):
                        return True
                    used.remove(i)
             
            return False
                
        return dfs(source)  
                
                
                
                
                
                
        