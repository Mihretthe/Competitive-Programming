ing = input()
from collections import Counter, defaultdict
b, s, c = list(map(int, input().split(" ")))
mb, ms, mc = list(map(int, input().split(" ")))
money = int(input())
cp = defaultdict(int)
ans = money
burg = 0
for ind in ing:
    cp[ind] +=1
 
# print(mb, b)
# print(cp)
while cp['B'] <= b and cp['C'] <= c and cp['S'] <= s:
    burg += 1
    b -= cp['B']
    c -= cp['C']
    s -= cp['S']
# print(burg)
fl = True
while (cp['B'] > 0 and b != 0) or (cp['C'] > 0 and c != 0)  or (cp['S'] and s != 0):
    if b < cp['B']:
        if mb*abs(cp['B']-b)<= money:
            money -= mb*abs(cp['B'] - b) 
            b += abs(cp['B']-b)
        else:
            fl = False
            break
    if c < cp['C']:
        if mc * abs(cp['C']-c) <= money:
            money -= mc*abs(cp['C']-c)
            c += abs(cp['C']-c)
        else:
            fl = False
            break
    if s < cp['S']:
        if (cp['S']-s) * ms <= money:
            money -= ms*abs(cp['S']-s)
            s += abs(cp['S']-s)
        else:
            fl = False
            break
 
    while cp['B'] <= b and cp['C'] <= c and cp['S'] <= s:
        burg += 1
        b -= cp['B']
        c -= cp['C']
        s -= cp['S']
    
# print(b, c, s)
# print(burg)
# print(fl, money)
if not fl:
    print(burg)
else:
    ans = money
    if cp['B'] != 0:
        ans += (mb*b)
    if cp['S'] != 0:
        ans += s * ms
    if cp['C'] != 0:
        ans += c *mc
    
 
    needed = (cp['B'] * mb) + (cp['C']* mc) + (cp['S'] * ms) 
    # print(ans, needed)
    print(ans//needed + burg)


