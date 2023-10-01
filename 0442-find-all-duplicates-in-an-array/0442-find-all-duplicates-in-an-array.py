class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        
        ans = []
        
        for i in counter:
            if counter[i] > 1:
                ans.append(i)
        return ans