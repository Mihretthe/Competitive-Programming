from collections import Counter
s = input()
t = input()
s_= s[::-1]
t_ = t[::-1]
indx = []
j = 0

dict = Counter(t) 
if t == s:
    print(0)
elif t in s:
    x = s.index(t)
    y = x +len(t)
    print(max(x,len(s)-y))
else:
    for i in range (len(t)):
        while j < len(s):
            if s_[j] == t_[i] and dict[s_[j]] > 0:
                if len(indx) == 0:
                    indx.append(len(s) -( j +1))
                    dict[s_[j]] -=1
                elif len(indx) > 0 and indx[-1] > len(s) - (j-1):
                    indx.append(len(s) -( j +1))
                    dict[s_[j]] -=1
            j +=1
            
    ans = 0
    indx_ =indx[::-1]
    print(indx_)
    for k in range (len(indx)):
        if k == 0:
            ans = max(ans,indx_[k] - 0)
        elif k == len(indx) -1:
            ans = max(ans,(len(s)-1) - indx_[k])
            break
        else:
            ans = max(ans,indx_[k+1]-indx_[k])
    print(ans)
       

