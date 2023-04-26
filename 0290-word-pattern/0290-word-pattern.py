class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c=[]
        for i in pattern:
            if c and i in c:
                continue
            c.append(i)
        a=s.split(" ")
        if len(pattern)!=len(a):
            return False
        f=list()
        for i in a:
            if f and i in f:
                continue
            f.append(i)
        b=dict(zip(c,f))
        n=""
        for i in pattern:
            if i in b.keys():
                n+=b[i]+" "
            else:
                continue
        return n[:-1]==s