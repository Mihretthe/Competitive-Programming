class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a = capacityA
        b = capacityB
        
        l = 0
        r = len(plants) - 1
        
        count = 0
        while l < r:
            if a < plants[l]:
                count += 1
                a = capacityA
            a -= plants[l]
            
            if b < plants[r]:
                count += 1
                b = capacityB
            b -= plants[r]
            
            l += 1
            r -= 1
        if l == r and a < plants[l] and b < plants[l]:
            count += 1
            
        return count
            