class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        slope = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')

        for i in range(2, n):
            x1, y1 = coordinates[i-1]
            x2, y2 = coordinates[i]
            new_slope = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
            if new_slope != slope:
                return False

        return True