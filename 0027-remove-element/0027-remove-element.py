class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=[]
        for i in nums:
            if i!=val:
                n.append(i)
        k=len(n)
        for i in range(k):
            nums[i]=n[i]
        return k
        