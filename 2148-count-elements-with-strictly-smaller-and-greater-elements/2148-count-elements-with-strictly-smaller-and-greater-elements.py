
class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        m=min(nums)
        mx=max(nums)
        ans=[i for i in nums if m<i<mx]
        return (len(ans))
               