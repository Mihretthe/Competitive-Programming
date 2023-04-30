class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        x=[n for n in nums if n%2==0]
        y=[n for n in nums if n%2==1]
        a=[]
        for i in range(len(nums)//2):
            a.append(x[i])
            a.append(y[i])
        return a