class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        length = len(points)
        count = 1
        index = 1
        end = points[0][1]

        while index < length:
            s, e = points[index]
            if s <= end:
                end = min(end, e)
            else:
                count += 1
                end = e
            index += 1
        
        return count
