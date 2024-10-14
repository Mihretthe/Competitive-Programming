class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0

        heap = []

        for i in nums:
            heappush(heap, -i)

        while heap and k > 0:
            val = -heappop(heap)
            score += val
            heappush(heap, -(ceil(val / 3)))
            k -= 1
        
        return score