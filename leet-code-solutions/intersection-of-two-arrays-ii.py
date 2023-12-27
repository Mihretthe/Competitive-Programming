class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        n = len(nums1)
        m = len(nums2)
        ans = []
        print(nums1, nums2)
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                yield nums1[i]
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if n > m:
                    i += 1
                else:
                    j += 1
