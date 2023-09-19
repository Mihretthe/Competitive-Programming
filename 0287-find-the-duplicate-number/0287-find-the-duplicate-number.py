class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        for i in nums:
            if counter[i] > 1:
                return i
            
       
    
                          