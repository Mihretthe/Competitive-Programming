class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dp = [[inf for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for u, v, w in edges:
            dp[u][v] = dp[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # if dp[i][k] + dp[k][j] <= min(distanceThreshold, dp[i][j]):
                    if dp[i][k] + dp[k][j] <= dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
        
        hashmap = defaultdict(list)
        for i in range(n):
            # count = dp[i].count(inf)
            count = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    count += 1
            hashmap[count].append(i)
            # print(*dp[i])
        
        mini = min(hashmap.keys())
        return max(hashmap[mini])
