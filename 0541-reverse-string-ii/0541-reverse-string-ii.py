class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        j=k
        s=[x for x in s]
        while i<len(s):
            s[i:j]=s[i:j][::-1]
            i+=2*k
            j+=(2*k)
        return "".join(s)