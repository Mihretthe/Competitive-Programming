class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        for i in range(1,len(nums)):
            comb=combinations(nums,i)
            a+=list((comb))
        a.append([])
        a.append(nums)
        return a
            