class Solution:
    def getRow(self, n: int) -> List[int]:
        def triangle(n, ans):
            
            for i in range(n + 1):
                if i > 0:
                    b = ans[-1]
                    a = [0]
                    for j in range(1,len(b)):
                        a.append(b[j] + b[j - 1])
                    a += [0]
                else:
                    a = [0,1,0]
                ans.append(a)
            return ans[-1][1:-1]
        return triangle(n, [])
                    