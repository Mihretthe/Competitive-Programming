class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        window = defaultdict(int)
        score = 0
        left = 0

        for right in range(len(nums)):
            
            if window[nums[right]] == 0:  
                score += nums[right]              
                window[nums[right]] += 1
            else:
                while left < len(nums) and nums[left] != nums[right]:
                    score -= nums[left]
                    window[nums[left]] -= 1
                    left += 1
                left += 1
                

            max_score = max(max_score, score)
        return max_score
