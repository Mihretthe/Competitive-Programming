class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=max(nums2)
        a=list()
        for i in range(len(nums1)):
            if nums1[i]==x or nums1[i]==nums2[-1]:
                a.append(-1)
            else:
                for j in range(len(nums2)-1):
                    if nums1[i]==nums2[j] and j!=len(nums2)-1 and nums1[i]<nums2[j+1]:
                        a.append(nums2[j+1])
                    elif nums1[i]==nums2[j] and j!=len(nums2)-1 and nums1[i]>nums2[j+1]:
                        c=0
                        for b in nums2[j+1:]:
                            if b>nums1[i]:
                                c=b
                                break
                        if c!=0:
                            a.append(c)
                        else:
                            a.append(-1)
        return a