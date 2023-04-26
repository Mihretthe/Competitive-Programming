class Solution:
    def dayOfYear(self, date: str) -> int:
        date=date.split("-")
        m=int(date[1]) 
        c=int(date[2])
        if m==1:
            return c
        b={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if int(date[0])%4==0 and int(date[0])%100!=0 or int(date[0])%100==0 and int(date[0])%400==0:
            b[2]=29
        n=0
        for i in range(1,m):
            n+=b[i]
        return n+c