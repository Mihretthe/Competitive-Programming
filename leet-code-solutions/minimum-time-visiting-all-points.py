class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        s = set()
        for i in range(1,len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            
            while x1 != x2 and y1 != y2:
                if x2 < x1:
                    x1 -= 1
                else:
                    x1 += 1
                if y2 < y1:
                    y1 -= 1
                else:
                    y1 += 1
                count += 1
            if x1 == x2:
                count += abs(y2 - y1)
            else:
                count += abs(x2 - x1)
        return count



            

