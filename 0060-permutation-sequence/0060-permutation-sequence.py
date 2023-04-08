class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perm=list((permutations(range(1,n+1))))
        b=""
        for i in perm[k-1]:
            b+=str(i)
        return b