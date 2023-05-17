class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=[]
        c=0
        for i in nums:
            if i==1:
                c+=1
                a.append(c)
            else:
                c=0
        if a:
            return max(a)
        else:
            return 0