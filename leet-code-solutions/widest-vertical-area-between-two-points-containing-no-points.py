class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        widest_area = 0

        for i in range(1, n):
            widest_area = max(widest_area, points[i][0] - points[i - 1][0])

        return widest_area
            
            