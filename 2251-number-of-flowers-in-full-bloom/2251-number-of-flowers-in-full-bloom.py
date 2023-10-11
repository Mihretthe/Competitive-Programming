class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = []
        end = []
        
        for s, e in flowers:
            start.append(s)
            end.append(e + 1)
        start.sort()
        end.sort()
        ans = []
        for i in people:
            a = bisect_right(start, i)    
            b = bisect_right(end, i)
            
            ans.append(a - b)
        
        
        return ans
        
        