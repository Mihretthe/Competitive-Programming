
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from collections import defaultdict
    

def solve():
    hour, minute = map(int, input().split(":"))
    ampm = ""

    if hour < 12:
        if hour == 0:
            hour = 12
        ampm = "AM"
    elif hour == 12:
        ampm = "PM"
    else:
        ampm = "PM"
        hour -= 12
    hr = str(hour) 
    mini = str(minute) 
    if len(hr) < 2:
        hr = "0" + hr
    if len(mini) < 2:
        mini = "0" + mini
    answer = hr + ":" + mini+ " " + ampm
    print(answer)





    

    
    
    
    
T = I()
for _ in range(T):   
    solve()
    