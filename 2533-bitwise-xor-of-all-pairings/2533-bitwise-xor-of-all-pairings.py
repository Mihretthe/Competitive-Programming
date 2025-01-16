class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)

        ans = 0

        if n % 2:
            for i in range(m):
                ans ^= nums2[i]
        
        if m % 2:
            for i in range(n):
                ans ^= nums1[i]

        return ans