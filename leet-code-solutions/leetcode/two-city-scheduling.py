class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        length = len(costs)
        collect = []

        for i in range(length):
            collect.append((i, costs[i][0] - costs[i][1]))

        collect.sort(key = lambda x : x[1])

        ans = 0
        for i in range(length):
            if i < (length // 2):
                ans += costs[collect[i][0]][0]
            else:
                ans += costs[collect[i][0]][1]
        return ans