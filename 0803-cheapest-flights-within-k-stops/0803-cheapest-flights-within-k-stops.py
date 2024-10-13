class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [inf] * n
        prev[src] = 0
        

        for _ in range(k + 1):
            relaxation = False
            curr = prev[:]
            for frm, to, price in flights:
                if prev[frm] != inf and curr[to] > prev[frm] + price:
                    curr[to] = prev[frm] + price
                    relaxation = True
            prev = curr[:]
            if not relaxation:
                break
                
        return prev[dst] if prev[dst] != inf else -1
