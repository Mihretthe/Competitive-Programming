class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0

        while len(nums) > 1:
            first = heappop(nums)
            if first >= k:
                break
            second = heappop(nums)
            calc = first * 2 + second
            heappush(nums, calc)
            operations += 1
            
        return operations


        


