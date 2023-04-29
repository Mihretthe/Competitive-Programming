a=""
for i in time:
print(a)
if i=="?":
if time.index(i) == 3:
print(yeay)
a+="5"
if time.index(i)==4:
a+="9"
if time.index(i)==0:
if int(time[1])>=4:
a+="1"
else:
a+="2"
if time.index(i)==1:
if time[0]=="2":
a+="3"
else:
a+="9"
else:
a+=i
return a