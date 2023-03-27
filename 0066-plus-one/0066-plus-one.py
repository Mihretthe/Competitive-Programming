class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        a=int(s)
        a+=1
        s=str(a)
        b=[]
        b.extend(s)
        x=[]
        for i in b:
            x.append(int(i))
        return x