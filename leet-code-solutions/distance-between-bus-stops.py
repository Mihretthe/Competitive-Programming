class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        s = sum(distance[min(start, destination): max(start, destination)])
        return min(s, sum(distance) - s)
        