class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current=current.split(":")
        correct=correct.split(":")
        current=list((map(int,current)))
        correct=list((map(int,correct)))
        a=correct[0]-current[0]
        a=(a*60)+(correct[1]-current[1])
        c=0
        while a>=1:
            if a>=60:
                n=a//60
                c+=n
                a=a%60
            elif a<60 and a>=15:
                n=a//15
                c+=n
                a=a%15
            elif a<15 and a>=5:
                n=a//5
                c+=n
                a%=5
            else:
                c+=a
                a=0
        return c
        