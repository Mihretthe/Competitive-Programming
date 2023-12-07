class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        losers = {}

        for winner, loser in matches:
            if loser in losers:
                losers[loser] += 1
            else:
                losers[loser] = 1
            if winner not in losers:
                losers[winner] = 0
        for i in losers:
            if losers[i] == 0:
              ans[0].append(i)
            elif losers[i] == 1:
              ans[1].append(i)
        ans[0].sort()
        ans[1].sort()

        
        return ans

        

        


