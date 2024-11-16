class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        def isConsecutive(array):
            
            for i in range(1, len(array)):
                if array[i] != array[i - 1] + 1:
                    return False

            return True

        ans = []
        
        for i in range(len(nums) - k + 1):
            array = nums[i: i + k]
            if isConsecutive(array):
                ans.append(array[-1])
            else:
                ans.append(-1)
            
        return ans