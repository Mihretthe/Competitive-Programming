class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
                
        for word in zip(*strs):            
            if list(word) != sorted(word) :
                count += 1
            
        
        return count