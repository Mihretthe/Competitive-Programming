class Solution:
    def countSegments(self, s: str) -> int:
        if s=="":
            return 0
        a=s.split(" ")
        b=[]
        for i in a:
            if i!="":
                b.append(i)
        return len(b)