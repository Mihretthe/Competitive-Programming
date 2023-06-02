class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        
        while i < j:
            h = min(height[i], height[j])
            max_area = max(max_area, h * (j - i))
            
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        
        return max_area