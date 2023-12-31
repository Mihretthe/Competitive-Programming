class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        bars = 0

        for i in costs:
            if coins > 0:
                bars += 1
            elif coins == 0:
                return bars 
            else:
                return bars - 1
            coins -= i
            
        return bars if coins >= 0 else bars - 1


            