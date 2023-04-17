class Solution:
    def calPoints(self, operations: List[str]) -> int:
        c=0
        a=[]
        for i in operations:
            if i=="C":
                a.pop()
            elif i=="D":
                a.append(2*a[-1])
            elif i=="+":
                a.append(a[-1]+a[-2])
            else:
                a.append(int(i))
        return sum(a)