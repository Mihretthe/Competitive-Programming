class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        length = len(weights)

        while left <= right:
            mid = (left + right) // 2

            count = 0
            total = 0
            for i in range(length):
                total += weights[i]
                if total > mid:
                    count += 1
                    total = weights[i]
                elif total == mid:
                    count += 1
                    total = 0
            if total:
                count += 1
            
            if count <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left

            
            
