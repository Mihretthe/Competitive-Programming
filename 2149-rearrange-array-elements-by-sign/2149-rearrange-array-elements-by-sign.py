class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[x for x in nums if x>=0]
        b=[x for x in nums if x<0]
        c=[]
        for i in range(len(nums)//2):
            c.append(a[i])
            c.append(b[i])
        return c
        
            