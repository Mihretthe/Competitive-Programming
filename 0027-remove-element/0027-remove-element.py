class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=[]
        m=[]
        for i in nums:
            if i!=val:
                n.append(i)
            else:
                m.append(i)
        k=len(n)
        for i in range(len(m)):
            m[i]="_"
        for i in range(k):
            nums[i]=n[i]
        return k
        