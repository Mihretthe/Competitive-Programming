class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        def findMax(l):
            maximum = 0
            for i, j, k in l:
                maximum = max(maximum, k)
            return maximum
        m = findMax(trips)
        prefix = [0] * (m + 1)
        
        
        for i , j , k in trips:
            
            prefix[j] += i
            prefix[k] -= i
        for i in range(1,m + 1):
            prefix[i] += prefix[i - 1]
            if prefix[i - 1] > capacity:
                return False
        return True
                