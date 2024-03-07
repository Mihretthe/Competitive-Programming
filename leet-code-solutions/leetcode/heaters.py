class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        max_radius = 0
        heaters.sort()

        for house in houses:
            left = 0
            right = len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] > house:
                    right = mid - 1
                else:
                    left = mid + 1

            if left == 0:
                max_radius = max(max_radius, abs(house - heaters[left]))
            elif left == len(heaters):
                max_radius = max(max_radius, abs(house - heaters[left - 1]))
            else:
                min_radius = min(abs(house - heaters[left]), abs(house - heaters[left - 1]))
                max_radius = max(max_radius, min_radius)

        
        return max_radius


