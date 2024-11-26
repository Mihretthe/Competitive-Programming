class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        answer = []
        for i in range(n):
            if i not in indegree:
                answer.append(i)
        if len(answer) == 1:
            return answer[0]
        return -1
