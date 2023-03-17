class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        a=list()
        b=list()
        for i in range(len(l)):
            b.append(sorted(nums[l[i]:r[i]+1]))
        for i in range(len(l)):
            if len(b[i])<1:
                a.append(True)
            else:
                x=b[i][1]-b[i][0]
                for j in range(len(b[i])-1):
                    if b[i][j+1]-b[i][j]!=x:
                        a.append(False)
                        break
                    elif b[i][j+1]-b[i][j]==x and j==len(b[i])-2:
                        a.append(True)
                        
        print(b)
        return a
        