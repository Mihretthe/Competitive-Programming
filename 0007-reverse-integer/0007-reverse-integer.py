class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        s="".join(reversed(s))
        if s[-1]=="-":
            s="-"+s
            s=s[:-1]
        x=int(s)
        a=bin(x)[2:]
        if len(a)>=32 and x>0 or x<0 and len(a)>32:
            return 0
        else:
            return x