class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=0
        for x in mat:
            n+=(x[mat.index(x)])
        l=0
        r=-1
        while l<len(mat) and r>=-len(mat):
            n+=mat[l][r]
            l+=1
            r-=1
        if len(mat)%2==0:
            return n
        else:
            return n-mat[len(mat)//2][len(mat)//2]
            
            