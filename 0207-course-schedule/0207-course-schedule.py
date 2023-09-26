class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         dictionary = {}
        
#         for a, b in prerequisites:
#             if a not in dictionary:
#                 dictionary[a] = []
#             dictionary[a].append(b)
#             if b in dictionary:
#                 dictionary[a].extend(dictionary[b])
        
#         for i in dictionary:
#             q = dictionary[i]
#             visited = set()
#             visited.add(i)
#             while q:
#                 n = q.pop()
#                 if n in dictionary and i in dictionary[n]:
#                     return False             
                
#                 if n in dictionary and n not in visited:
#                     q.extend(dictionary[n])
#                     visited.add(n)
#                 if i in q:
#                     return False
                    
#         return True
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        
        visited = [0] * numCourses
        
        def hasCycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False
            
            visited[course] = 1
            for prerequisite in graph[course]:
                if hasCycle(prerequisite):
                    return True
            visited[course] = 2
            
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True