class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        l=0
        r=len(num)-1
        if len(num)%2!=0:
            return num[(r+l)//2]
        else:
            return (num[(r+l)//2]+num[(r+l)//2+1])/2