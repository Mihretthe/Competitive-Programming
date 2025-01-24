class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        
        edges = defaultdict(list)
        
        for i in range(len(graph)):
            indegree[i] += len(graph[i])
            for j in graph[i]:
                edges[j].append(i)
        
        deck = deque()

        for i in range(len(graph)):
            if not indegree[i]:
                deck.append(i)
        
       

        
        answer = []

        while deck:
            node = deck.popleft()

            for i in edges[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    deck.append(i)
            answer.append(node)

        return sorted(answer)