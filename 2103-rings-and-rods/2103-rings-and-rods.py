class Solution:
    def countPoints(self, rings: str) -> int:
        a=set()
        for i in rings:
            if i.isnumeric():
                a.add(i)
        b=[]
        for i in range(0,len(rings),2):
            b.append(rings[i:i+2])
        n=list(a)
        x=0
        
        for i in n:
            y=set()
            for j in b:
                if i in j:
                    y.add(j[0])
            if len(y)==3:
                x+=1
        return x