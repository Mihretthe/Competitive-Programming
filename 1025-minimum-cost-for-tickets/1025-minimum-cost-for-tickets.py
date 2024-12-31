class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        length = len(days)

        memo = {}
        def dp(pre, cost, index):
            if index == length:
                return 0
            if (pre, cost, index) not in memo:           
            
                number = 0

                if cost == 0:
                    number = 1
                elif cost == 1:
                    number = 7
                else:
                    number = 30
                
                if pre + number > days[index]:
                    return dp(pre, cost, index + 1)
                
                ones = costs[0] + dp(days[index], 0, index + 1)
                seven = costs[1] + dp(days[index], 1, index + 1)
                thirty = costs[2] + dp(days[index], 2, index + 1)

                memo[(pre, cost, index)] = min(ones, seven, thirty)
            
            return memo[(pre, cost, index)]

        return dp(0, 0, 0)

            
            