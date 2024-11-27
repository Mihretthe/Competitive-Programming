class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        for i in range(n - 1):
            graph[i].append(i + 1)
        
        answer = []
        
        for u, v in queries:
            graph[u].append(v)

            deck = deque([(0, 0)])
            visited = set([0])
            while deck:
                node, level = deck.popleft()
                if node == n - 1:
                    answer.append(level)
                    break
                for friend in graph[node]:
                    if friend not in visited:
                        visited.add(friend)
                        deck.append((friend, level + 1))
        
        return answer

