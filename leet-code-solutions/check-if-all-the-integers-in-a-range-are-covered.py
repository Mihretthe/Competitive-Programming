class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range(left, right + 1):
            flag = False
            for l,r in ranges:
                if i in range(l,r + 1):
                    flag = True
            if flag == False:
                return False
        return True
