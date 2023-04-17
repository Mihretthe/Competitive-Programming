class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        b=""
        c=[]
        for i in s:
            if i.isalnum():
                b+=i.upper()
        i=0
        b=b[::-1]
        while i<len(b):
            n=b[i:i+k]
            c.append(n[::-1])
            i+=k
        c=c[::-1]
        return "-".join(c)