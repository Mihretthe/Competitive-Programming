class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        a=[i for i in nums1 if i in nums2]
        if a:
            return min(a)
        n=min(nums1)
        m=min(nums2)
        return (10*min(n,m))+max(n,m)
