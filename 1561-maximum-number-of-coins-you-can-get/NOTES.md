piles.sort()
bob=alice=me=0
for i in range(len(piles)):
if i%3==0:
bob+=piles[i]
elif i%3==1:
me+=piles[i]
else:
alice+=piles[i]
print(bob)
print(alice)
print(me)
return me
my error was that i sorted the list before divide it to 3 3 list of lists
​
​
so first divide the list to lists with 3 3
for i in range(int(len(piles)/3))
if i>0
a.append(num[i:i3])
else
a.append(num[i:3]
​
​
​
​