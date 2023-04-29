class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0]=="?":
            if time[1].isnumeric() and int(time[1])>=4:
                a="1"
            else:
                a="2"
        else:
            a=time[0]
        if time[1]=="?":
            if int(a[0])==2:
                a+="3"
            else:
                a+="9"
        else:
            a+=time[1]
        a+=time[2]
        if time[3]=="?":
            a+="5"
        else:
            a+=time[3]
        if time[4]=="?":
            a+="9"
        else:
            a+=time[4]
        return a