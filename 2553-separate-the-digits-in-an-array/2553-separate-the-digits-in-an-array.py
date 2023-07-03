class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            b=[int(j) for j in str(i)]
            a+=b
        return a 