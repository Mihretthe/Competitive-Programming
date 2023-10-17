class Solution:
    def getRow(self, n: int) -> List[int]:
        def triangle(n, ans):
            
            for i in range(n + 1):
                if i > 0:
                    
                    a = [0]
                    for j in range(1,len(ans)):
                        a.append(ans[j] + ans[j - 1])
                    a += [0]
                else:
                    a = [0,1,0]
                ans = a
            return ans[1:-1]
        return triangle(n, [])
                    