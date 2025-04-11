class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        source = 0
        destination = len(graph) - 1
        answer = []
        

        def backtrack(node, path):

            if node == destination:
                answer.append(path[:])
                return

            for neighbour in graph[node]:
                path.append(neighbour)
                backtrack(neighbour, path[:])
                path.pop()
            
        backtrack(0, [0])
        return answer

    