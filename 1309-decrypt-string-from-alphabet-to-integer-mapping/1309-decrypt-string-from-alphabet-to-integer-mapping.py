class Solution:
    def func(self,a):
        l=string.ascii_lowercase
        return str(l.index(a)+1) if l.index(a)+1<10 else str(l.index(a)+1)+"#"
    def freqAlphabets(self, s: str) -> str:
        l=string.ascii_lowercase
        m=map(self.func,l)
        n=list(m)
        r=len(s)-1
        a=[]
        while r>=0:
            if s[r]=="#":
                a.append(s[r-2:r+1])
                r-=3
            else:
                a.append(s[r])
                r-=1
        a=a[::-1]
        z=""
        for i in a:
            z+=l[n.index(i)]
        return z