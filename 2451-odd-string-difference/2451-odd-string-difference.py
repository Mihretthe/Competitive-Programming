class Solution:          
    def oddString(self, words: List[str]) -> str:
        s="abcdefghijklmnopqrstuvwxyz"
        b=[]
        c=[]
        for i in words:
            for j in range(1,len(i)):
                a=(s.index(i[j])-s.index(i[j-1]))
                b.append(a)
                if len(b)==len(i)-1:
                    c.append(b)
                    b=[]
        d=[c.index(x) for x in c if c.count(x)==1]
        return words[d[0]]