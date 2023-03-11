class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # x=sqrt()
        y=list(list())
        z=list(list())
        x=0
        for i in range(len(points)):
            x=round(sqrt(points[i][0]**2 + points[i][1]**2),3)
            y.append((x,i))
        y.sort()
        print(y)
        for j in range(k):
            z.append(points[y[j][1]])
        print(z)
        return z
            
        