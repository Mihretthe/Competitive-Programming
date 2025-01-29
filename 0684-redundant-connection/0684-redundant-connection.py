class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {i:i for i in range(1, len(edges) + 1)}

      
        
        def union(x, y):
            parentX = parents[x]
            parentY = parents[y]

            if parentX != parentY:
                for node in parents:
                    if parents[node] == parentY:
                        parents[node] = parentX
            else:
                return [x, y]

        for u, v in edges:
            answer = union(u, v)
            if answer:
                return answer

        return answer