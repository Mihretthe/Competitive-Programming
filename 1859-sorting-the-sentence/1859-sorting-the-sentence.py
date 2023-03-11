class Solution:
    def sortSentence(self, s: str) -> str:
        x=s.split(" ")
        # print(x)
        y=list(list())
        j=list()
        for i in range(len(x)):
            z=int(x[i][len(x[i])-1])
            y.append((z,i))
        # print(y)
        y.sort()
        for i in range(len(x)):
            j.append(x[y[i][1]]) 
            j[i]=j[i][:len(j[i])-1]
        n=" ".join(j)
        # print(y)
        # print(n)
        return n
        
            
        