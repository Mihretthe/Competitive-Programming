# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, m: 'MountainArray') -> int:
        n = m.length()
        
        idx = -1
        l = 0
        r = n - 1
        peakIdx = 0
        while l <= r:
            mid = (l + r) // 2
            
            a = m.get(mid)       
            b = m.get(mid - 1)
            c = m.get(mid + 1)
            
            if a > c and a > b:
                peakIdx = mid
                
                break
                
            elif a > c and b > a:
                r = mid
            else:
                l = mid + 1                 
        l = 0
        while l < peakIdx:
            mid = (l + peakIdx) // 2
            a =  m.get(mid)
            if a == target:
                idx = mid
                break
            elif a < target:
                l = mid + 1
            elif a > target:
                peakIdx = mid  
        if idx != -1:
            return idx
        else:
            l = peakIdx
            n -= 1
            while l <= n:
                mid = (l + n) // 2
                a =  m.get(mid)
                if a == target:
                    idx = mid
                    break
                elif a > target:
                    l = mid + 1
                elif a < target:
                    n = mid - 1
            return idx