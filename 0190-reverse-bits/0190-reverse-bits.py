class Solution:
    def reverseBits(self, n: int) -> int:
        a=bin(n)[2:]
        a="".join(reversed(a))
        b=32-len(a)
        i=0
        while i<b:
            a+="0"
            i+=1
        return int(a,2)