class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm=list((permutations(nums)))
        a=[]
        for i in perm:
            if a and i in a:
                continue
            else:
                a.append(i)
        return a