class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)

        def check(mid):
            count = 0

            for num in nums:
                count += ceil(num / mid) - 1
            
            return count <= maxOperations

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
