class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        r = set(range(1,k+1))
        j = len(nums) - 1
        visit = set()
        while j >= 0 and k > 0:
            if nums[j] in r and nums[j] not in visit:
                visit.add(nums[j])
                k -= 1
            j -= 1
        j += 1
        return len(nums) - j 
            