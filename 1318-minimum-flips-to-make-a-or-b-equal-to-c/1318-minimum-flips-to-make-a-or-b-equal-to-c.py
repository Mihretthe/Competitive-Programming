class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a=format(a,"04b")
        b=format(b,"04b")
        c=format(c,"04b")
        n=max(len(a),len(b),len(c))
        s="0"*(n-len(a))
        a=s+a
        s="0"*(n-len(c))
        c=s+c
        s="0"*(n-len(b))
        b=s+b
        count=0
        for i in range(n):
            if a[i]==b[i]==c[i] or a[i]=="1" and b[i]=="0" and c[i]=="1" or a[i]=="0" and b[i]=="1" and c[i]=="1":
                continue
            elif a[i]==b[i]=="1" and c[i]=="0":
                count+=2
            elif a[i]==b[i]=="0" and c[i]=="1":
                count+=1
            elif  a[i]=="1" and b[i]=="0" or a[i]=="0" and b[i]=="1" and c[i]=="0":
                count+=1
            else:
                count+=1
        return count