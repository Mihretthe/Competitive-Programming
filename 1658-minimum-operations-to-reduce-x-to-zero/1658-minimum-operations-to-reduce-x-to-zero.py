class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
    
        totalSum = sum(nums)
        targetSum = totalSum - x

        if targetSum == 0:
            return len(nums)

        n = len(nums)
        left = 0
        currentSum = 0
        minOperations = float('inf')

        for right in range(n):
            currentSum += nums[right]

            while currentSum > targetSum and left <= right:
                currentSum -= nums[left]
                left += 1

            if currentSum == targetSum:
                minOperations = min(minOperations, n - (right - left + 1))

        if minOperations == float('inf'):
            return -1
        else:
            return minOperations
